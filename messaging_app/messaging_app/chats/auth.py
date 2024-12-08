from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CustomJWTAuthentication(JWTAuthentication):
    """
    Custom JWT Authentication to add extra checks or handle errors differently.
    """

    def authenticate(self, request):
        try:
            # Call the parent method to perform standard JWT authentication
            validated_data = super().authenticate(request)
            if validated_data is None:
                raise AuthenticationFailed("Invalid token or no token provided.")
            return validated_data
        except Exception as e:
            raise AuthenticationFailed(f"Authentication failed: {str(e)}")
