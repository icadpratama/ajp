from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Event

# Create your views here.
def list(request):
    qs = Event.objects.all().published() # queryset -> list of python object
    if request.user.is_authenticated:
        my_qs = Event.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'event.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def detail(request):
    return HttpResponse("<h1>Event Detail</h1>")