from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.news_list, name='news_list_url'),
    path('news/<str:slug>/', views.news_detail, name='news_detail_url'),
]