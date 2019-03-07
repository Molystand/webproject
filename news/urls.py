from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.news_list, name='list_news')
]