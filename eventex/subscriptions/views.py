# coding: utf-8
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.views.generic import DetailView, CreateView


class SubscriptionCreate(CreateView):
    model = Subscription
    form_class = SubscriptionForm


class SubscriptionDetail(DetailView):
    model = Subscription
