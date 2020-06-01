from django.shortcuts import render
from django.http import HttpResponse


def home(response):
    return render(response, "main/base.html", {})
def mainpage(response):
    return render(response, "main/mainpage.html", {})
