from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', news_list, name='news_list_url'),
    path('news/<str:slug>/', NewsDetail.as_view(), name='news_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),

]