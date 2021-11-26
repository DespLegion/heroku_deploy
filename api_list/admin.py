from django.contrib import admin
from .models import ApiList


# Register your models here.
class ApiListShow(admin.ModelAdmin):
    list_display = ('id', 'request_type', 'name', 'api_url', 'add_date', 'activ')
    list_display_links = ('name',)
    list_filter = ('id', 'request_type', 'add_date', 'activ')
    search_fields = ('id', 'name', 'api_url', 'add_date')


admin.site.register(ApiList, ApiListShow)
