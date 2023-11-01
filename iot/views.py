from django.shortcuts import render
import sys, os, django

# django.setup()
import iot.iot


def index(request):
    return render(request, 'index.html')


def fire(request):
    return render(request, 'fire.html')


def accident(request):
    return render(request, 'accident.html')


def robber(request):
    return render(request, 'robber.html')
