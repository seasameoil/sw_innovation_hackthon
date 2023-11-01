from django.shortcuts import render
import sys, os, django

# django.setup()
import iot.iot


def index(request):
    context = {'text': "hello world"}
    return render(request, 'index.html')


def bus1(request):
    return render(request, 'u_bus1.html')


def bus2(request):
    return render(request, 'u_bus2.html')


def bus3(request):
    return render(request, 'u_bus3.html')


def bus4(request):
    return render(request, 'u_bus4.html')


def admin(request):
    return render(request, 'video.html')


def admin_bus1(request):
    return render(request, 'a_bus1.html')


def admin_bus2(request):
    return render(request, 'a_bus2.html')


def admin_bus3(request):
    return render(request, 'a_bus3.html')


def admin_bus4(request):
    return render(request, 'a_bus4.html')
