from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', news_list, name='news_list_url'),
    path('news/<str:slug>/', news_detail, name='news_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail_url'),

]