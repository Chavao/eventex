# coding: utf-8
from django.contrib.auth import get_user_model
from django.test import TestCase
from eventex.myauth.backends import EmailBackend


class EmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='henrique',
                                      email='henrique@bastos.net',
                                      password='abracadabra')
        self.backend = EmailBackend()

    def test_authenticate_with_email(self):
        user = self.backend.authenticate(email='henrique@bastos.net',
                                         password='abracadabra')
        self.assertIsNotNone(user)
