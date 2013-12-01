# coding: utf-8
from django.test import TestCase


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """
        Get /inscricao/ must return status code 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Response should be rendered by template.
        """
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
