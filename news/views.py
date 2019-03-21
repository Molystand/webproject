from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from .models import News, Tag, Comment
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, NewsForm, CommentForm


def news_list(request):
    """Вывод всех статей
    """
    news = News.objects.all()
    return render(request, 'news/index.html', context={'news': news})


class NewsDetail(ObjectDetailMixin, View):
    model = News
    template = 'news/news_detail.html'


class NewsCreate(ObjectCreateMixin, View):
    model_form = NewsForm
    template = 'news/news_create_form.html'


class NewsUpdate(ObjectUpdateMixin, View):
    model = News
    model_form = NewsForm
    template = 'news/news_update_form.html'


class NewsDelete(ObjectDeleteMixin, View):
    model = News
    template = 'news/news_delete_form.html'
    redirect_url = 'news_list_url'


def tags_list(request):
    """Все теги
    """
    tags = Tag.objects.all()
    return render(request, 'news/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'news/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'news/tag_create_form.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'news/tag_update_form.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'news/tag_delete_form.html'
    redirect_url = 'tags_list_url'
