import rest_framework_simplejwt.authentication
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.exceptions import InvalidToken


class JWTAuthenticationMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

        def __call__(self, request):
            if request.path.startswith("/admin/"):
                return self.get_response(request)

            user, auth_token = self.authenticate(request)
            request.user = user
            request.auth = auth_token
            response = self.get_response(request)
            return response

    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION", None)

        if not token:
            return AnonymousUser(), None

        try:
            token = token.split(" ")[1]
            validated_token = rest_framework_simplejwt.authentication.JWTAuthentication().get_validated_token(token)
            user = rest_framework_simplejwt.authentication.JWTAuthentication().get_user(validated_token)
        except InvalidToken:
            return AnonymousUser(), None

        return user, validated_token
