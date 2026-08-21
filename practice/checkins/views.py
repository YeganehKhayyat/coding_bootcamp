from django.shortcuts import render
from django.http import HttpResponse


def home(requests):
    # return HttpResponse("Welcome to my website")
    return render(requests, "checkins/home.html")
