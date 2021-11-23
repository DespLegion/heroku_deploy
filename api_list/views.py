from django.shortcuts import render
from django.views import View

from .models import ApiList
# Create your views here.


class ApiListView(View):
    """Вывод списка API"""
    def get(self, request):
        apis = ApiList.objects.all()
        return render(request, 'api_list/main_page.html', {'api_list': apis})
