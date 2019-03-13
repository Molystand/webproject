from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import News, Tag
from .utils import ObjectDetailMixin
from .forms import TagForm


def news_list(request):
    """Вывод всех статей
    """
    news = News.objects.all()
    return render(request, 'news/index.html', context={'news': news})


class NewsDetail(ObjectDetailMixin, View):
    model = News
    template = 'news/news_detail.html'


def tags_list(request):
    """Все теги
    """
    tags = Tag.objects.all()
    return render(request, 'news/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'news/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'news/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            # Если форма валидна, добавляем тег
            # в базу и переходим на страницу тега
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'news/tag_create.html', context={'form': bound_form})