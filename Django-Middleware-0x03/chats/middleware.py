import logging
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden

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