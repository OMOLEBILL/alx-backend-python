import logging
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin

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
