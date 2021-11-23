from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiListView.as_view()),
    path('/', views.ApiListView.as_view())
]