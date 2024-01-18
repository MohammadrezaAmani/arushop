import rest_framework_simplejwt
from django.contrib.auth.models import AnonymousUser


def get_user(request):
    token = request.META.get("HTTP_AUTHORIZATION", None)
    if not token:
        return AnonymousUser()
    try:
        token = token.split(" ")[1]
        token = rest_framework_simplejwt.authentication.JWTAuthentication().get_validated_token(token)
    except rest_framework_simplejwt.exceptions.InvalidToken:
        return AnonymousUser()
    try:
        user = rest_framework_simplejwt.authentication.JWTAuthentication().get_user(token)
    except rest_framework_simplejwt.exceptions.InvalidToken:
        return AnonymousUser()
    return user


class AuthMiddleware:
    def __init__(self, get_response, *args, **kwargs):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        request.user = get_user(request)
        response = self.get_response(request)
        return response
