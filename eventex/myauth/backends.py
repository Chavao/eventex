# coding: utf-8
from django.contrib.auth import get_user_model


class EmailBackend(object):
    def authenticate(self, email, password, **kwargs):
        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None

        if not user.check_password(password):
            return None
        return user
