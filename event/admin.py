from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Event

class EventModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ["title", "thumbnail", "updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = Event

admin.site.register(Event, EventModelAdmin)