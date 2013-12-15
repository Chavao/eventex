# coding: utf-8
from django.conf.urls import patterns, include, url
from eventex.subscriptions.views import SubscriptionDetail, SubscriptionCreate


urlpatterns = patterns('',
    url(r'^$', SubscriptionCreate.as_view(), name='subscribe'),
    url(r'^(?P<pk>\d+)/$', SubscriptionDetail.as_view(), name='detail'),
)
