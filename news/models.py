from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
User = get_user_model()


class Tag(models.Model):
    title = models.CharField('Тег', max_length=50)
    slug = models.SlugField('Slug', max_length=50,unique=True)


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
    slug = models.SlugField('Slug', max_length=120, unique=True)
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


    def __str__(self):
        return self.title