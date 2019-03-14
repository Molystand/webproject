from django.shortcuts import render
from django.views.generic import View

from .models import News, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, NewsForm


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
