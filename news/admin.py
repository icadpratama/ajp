from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Category, News

class NewsModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ["title", "thumbnail", "updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = News

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    class Meta:
        model = Category

admin.site.register(News, NewsModelAdmin)
admin.site.register(Category, CategoryAdmin)