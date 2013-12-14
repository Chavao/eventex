# coding: utf-8
from django.shortcuts import render
from eventex.core.models import Speaker


def home(request):
    return render(request, 'index.html')


def speaker_detail(request, slug):
    speaker = Speaker.objects.get(slug=slug)
    context = {'speaker': speaker}
    return render(request, 'core/speaker_detail.html', context)
