from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import News

# Create your views here.
def list(request):
    qs = News.objects.all().published() # queryset -> list of python object
    if request.user.is_authenticated:
        my_qs = News.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'news.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def detail(request):
    return HttpResponse("<h1>News Detail</h1>")