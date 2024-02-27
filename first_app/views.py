from django.shortcuts import render
from django.http import HttpResponse
from .python_robotcontroller.game import *
import pygame
import socket

# Create your views here.

def index(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')
def information(request):
    return render(request, 'information.html')
def settings(request):
    return render(request, 'settings.html')

def start(request):
    print("starting robot..")
    start_robot()
    return HttpResponse("")

def camera(request):
    print("opening camera..")
    return HttpResponse("")

def sound(request):
    print("playing sound..")
    return HttpResponse("")


def shutdown(request):
    print("shutting down..")
    return HttpResponse("")
