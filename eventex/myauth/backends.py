# coding: utf-8
from django.contrib.auth import get_user_model


class EmailBackend(object):
    def authenticate(self, email, password, **kwargs):
        UserModel = get_user_model()
        user = UserModel.objects.get(email=email)
        return user
