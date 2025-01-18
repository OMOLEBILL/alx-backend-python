import logging
from datetime import datetime, timedelta
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from collections import defaultdict, deque

# Configure a logger for this module
logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(MiddlewareMixin):
    """
    Logs each request with a timestamp, user, and path.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated or anonymous
        user = request.user if request.user.is_authenticated else "AnonymousUser"

        # Log the desired info: "timestamp - User: X - Path: Y"
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")

        # Process the request
        response = self.get_response(request)
        return response

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get current server time
        now = datetime.now().time()

        # Define restricted hours: outside 6PM to 9PM
        start_time = now.replace(hour=18, minute=0, second=0, microsecond=0)
        end_time = now.replace(hour=21, minute=0, second=0, microsecond=0)

        # If current time is outside the allowed window, block access
        if not (start_time <= now < end_time):
            return HttpResponseForbidden("Access denied. Chat is only available between 6PM and 9PM.")

        # Otherwise, proceed as normal
        response = self.get_response(request)
        return response
    
class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Dictionary to track datetimes of POST requests per IP:
        # { ip_address: deque([datetime1, datetime2, ...]) }
        self.requests_per_ip = defaultdict(lambda: deque())

        # Rate limit parameters
        self.MESSAGE_LIMIT = 5                
        self.TIME_WINDOW = timedelta(minutes=1)  

    def __call__(self, request):
        # Check if this is a POST request to the messaging endpoint
        if request.method == "POST" and "/api/messages/" in request.path:
            # Get the client's IP address
            ip_address = self.get_client_ip(request)

            # Get current datetime
            now = datetime.now()

            # Get or initialize deque for this IP
            timestamps = self.requests_per_ip[ip_address]

            # Remove outdated datetimes beyond the TIME_WINDOW
            while timestamps and (now - timestamps[0]) > self.TIME_WINDOW:
                timestamps.popleft()

            # Check if limit is reached
            if len(timestamps) >= self.MESSAGE_LIMIT:
                return HttpResponseForbidden(
                    "Rate limit exceeded. Please wait before sending more messages."
                )

            # Record this request's datetime
            timestamps.append(now)

        # Proceed with processing the request normally
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        """Helper function to get client's IP address."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # In case of multiple proxies, the first IP is the client
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip