# coding: utf-8
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def speaker_detail(request, slug):
    return render(request, 'core/speaker_detail.html')

