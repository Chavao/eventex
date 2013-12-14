# coding: utf-8
from django.db import models


class EmailContactManager(models.Manager):
    def get_queryset(self):
        qs = super(EmailContactManager, self).get_queryset()
        qs = qs.filter(kind='E')
        return qs


class PhoneContactManager(models.Manager):
    def get_queryset(self):
        qs = super(PhoneContactManager, self).get_queryset()
        qs = qs.filter(kind='P')
        return qs


class FaxContactManager(models.Manager):
    def get_queryset(self):
        qs = super(FaxContactManager, self).get_queryset()
        qs = qs.filter(kind='F')
        return qs
