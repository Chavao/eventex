# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r


class TalkListTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        """
        GET must result in 200.
        """
        self.assertEqual(200, self.resp.status_code)
