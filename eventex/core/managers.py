# coding: utf-8
from django.db import models


class EmailContactManager(models.Manager):
    def get_queryset(self):
        qs = super(EmailContactManager, self).get_queryset()
        qs = qs.filter(kind='E')
        return qs
