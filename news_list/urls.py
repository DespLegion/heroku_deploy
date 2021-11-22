from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsListView.as_view()),
    path('news/<int:pk>/', views.NewsDetailView.as_view())
]