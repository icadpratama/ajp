from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Event

# Create your views here.
def list(request):
    qs_list = Event.objects.all().published() # queryset -> list of python object
    paginator = Paginator(qs_list, 2)
    page_number = request.GET.get('page')
    qs = paginator.get_page(page_number)
    template_name = 'event.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def detail(request):
    return HttpResponse("<h1>Event Detail</h1>")