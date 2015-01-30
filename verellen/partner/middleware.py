from django.contrib import auth
import utils

class UserExpiryDateMiddleware(auth.middleware.AuthenticationMiddleware):
    def process_request(self, request):
        user = request.user
        if not user.is_anonymous() and user.is_authenticated:
            if utils.user_is_expired(user):
                auth.logout(request)
