from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, "news.html", {})

def detail(request):
    return HttpResponse("<h1>News Detail</h1>")