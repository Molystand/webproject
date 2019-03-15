from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', news_list, name='news_list_url'),
    path('news/create/', NewsCreate.as_view(), name='news_create_url'),
    path('news/<str:slug>/', NewsDetail.as_view(), name='news_detail_url'),
    path('news/<str:slug>/update/', NewsUpdate.as_view(), name='news_update_url'),
    path('news/<str:slug>/delete/', NewsDelete.as_view(), name='news_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
]
