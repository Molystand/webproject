from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import News, Tag
from .utils import ObjectDetailMixin


def news_list(request):
    """Вывод всех статей
    """
    news = News.objects.all()
    return render(request, 'news/index.html', context={'news': news})


class NewsDetail(ObjectDetailMixin, View):
    model = News
    template = 'news/news_detail.html'
    # def get(self, request, slug):
    #     news = get_object_or_404(News, slug__iexact=slug)
    #     return render(request, 'news/news_detail.html', context={'news': news})


def tags_list(request):
    """Все теги
    """
    tags = Tag.objects.all()
    return render(request, 'news/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'news/tag_detail.html'
    # def get(self, request, slug):
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'news/tag_detail.html', context={'tag': tag})