from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News
from .serializers import NewsListSerializer, DetailNewsSerializer
# Create your views here.


class NewsListView(APIView):
    """Вывод списка всех новостей"""
    def get(self, request):
        news = News.objects.all()
        serializer = NewsListSerializer(news, many=True)
        return Response(serializer.data)

class NewsDetailView(APIView):
    """Вывод детальной страницы новости"""

    def get(self, request, pk):
        news = News.objects.get(id=pk)
        serializer = DetailNewsSerializer(news)
        return Response(serializer.data)