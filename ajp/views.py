from django.http import HttpResponse
from django.shortcuts import render

# Dont Repeat Yourself = DRY


def home_page(request):
    return render(request, "home.html", {})

def contact_page(request):
    return render(request, "contact.html", {})