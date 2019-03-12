from django.shortcuts import render
from news.models import News, Tag


def news_list(request):
    """Вывод всех статей
    """
    news = News.objects.all()
    return render(request, 'news/index.html', context={'news': news})


def news_detail(request, slug):
    """Вывод конкретной статьи
    """
    news = News.objects.get(slug__iexact=slug)
    return render(request, 'news/news_detail.html', context={'news': news})


def tags_list(request):
    """Все теги
    """
    tags = Tag.objects.all()
    return render(request, 'news/tags_list.html', context={'tags': tags})


def tag_detail(request, slug):
    """Вывод конкретного тега
    """
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'news/tag_detail.html', context={'tag': tag})