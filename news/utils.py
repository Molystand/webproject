from django.shortcuts import render, get_object_or_404, redirect
from .models import *


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj,
                                                       'admin_object': obj, 'detail': True})


class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        # Проверка прав пользователя (через группу),
        # редирект на главную, если прав недостаточно
        if not (request.user.groups.filter(name='Editors').exists() or request.user.is_staff):
            return redirect('news_list_url')
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        bound_form.instance.user = self.request.user

        if bound_form.is_valid():
            # Если форма валидна, добавляем объект
            # в базу и переходим на его страницу
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        # Проверка прав пользователя (должен быть админом),
        # редирект на главную, если прав недостаточно
        if not request.user.is_staff:
            return redirect('news_list_url')
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        # Проверка прав пользователя (должен быть админом),
        # редирект на главную, если прав недостаточно
        if not request.user.is_staff:
            return redirect('news_list_url')
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
