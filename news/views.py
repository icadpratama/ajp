from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import News

# Create your views here.
def list(request):
    qs_list = News.objects.all().published()
    paginator = Paginator(qs_list, 6)
    page_number = request.GET.get('page')
    qs = paginator.get_page(page_number)
    template_name = 'news.html'
    context = {
        'object_list': qs
    }
    return render(request, template_name, context)

def detail(request, slug):
    obj = get_object_or_404(News, slug=slug)
    template_name = 'news/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)