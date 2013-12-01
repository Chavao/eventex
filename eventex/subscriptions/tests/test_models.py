# coding: utf-8
from django.test import TestCase
from datetime import datetime
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Henrique Bastos',
            cpf='12345678901',
            email='henrique@bastos.net',
            phone='21-96186180'
        )

    def test_create(self):
        """
        Subscription must have name, cpf, email, phone
        """
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        """
        Subscription must have automatica created_at.
        """
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)
