from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time

User = get_user_model()


def gen_slug(s):
    """Генерирует slug из заголовка
    """
    new_slug = slugify(s, allow_unicode=True)
    # Т.к. заголовок может быть не уникальным,
    # добавим к slug настоящее время (в секундах с 1970 года)
    return new_slug + '-' + str(int(time()))


class Tag(models.Model):
    title = models.CharField('Тег', max_length=50)
    slug = models.SlugField('Slug', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def get_absolute_url(self):
        """Ссылка на конкретный тег
        """
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class News(models.Model):
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=120)
    slug = models.SlugField('Slug', max_length=120, blank=True, unique=True)
    text_preview = models.TextField('Текстовое превью', max_length=350)
    picture_preview_path = models.CharField('Изображение на превью', max_length=150)
    text = models.TextField('Текст статьи')
    publish_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='news')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self):
        """Ссылка на конкретную статью
        """
        return reverse('news_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """Переопределение функции сохранения,
        чтобы генерация slug происходила только при
        создании и сохранении модели в бд
        """
        # Пока экземпляр не сохранён в бд, у него нет id
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
