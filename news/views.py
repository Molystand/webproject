from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse

from .models import News, Tag, Comment
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, NewsForm, CommentForm


def news_list(request):
    """Вывод всех статей
    """
    news = News.objects.all()
    return render(request, 'news/index.html', context={'news': news})


class NewsDetail(View):
    def get(self, request, slug):
        news = get_object_or_404(News, slug__iexact=slug)
        comments = Comment.objects.filter(news=news)
        form = CommentForm()
        return render(request, 'news/news_detail.html', context={'news': news, 'comments': comments, 'form': form})

    def post(self, request, slug):
        bound_form = CommentForm(request.POST)

        if bound_form.is_valid():
            new_comment = bound_form.save(commit=False)
            new_comment.news = News.objects.get(slug__iexact=slug)
            new_comment.user = request.user
            new_comment.save()
            return redirect('news_detail_url', slug)
        return render(request, 'news/news_detail.html', context={'form': bound_form})


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


class Login(FormView):
    form_class = AuthenticationForm
    template_name = 'news/login_form.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        return super(Login, self).form_invalid(form)


class Registration(FormView):
    form_class = UserCreationForm
    template_name = 'news/registration_form.html'
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super(Registration, self).form_valid(form)

    def form_invalid(self, form):
        return super(Registration, self).form_invalid(form)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('news_list_url')
