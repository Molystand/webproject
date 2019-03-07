from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Tag(models.Model):
    title = models.CharField('Тег', max_length=20)


    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


    def __str__(self):
        return self.title




class News(models.Model):
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=120)
    text_preview = models.TextField('Текстовое превью', max_length=350)
    picture_preview_path = models.CharField('Изображение на превью', max_length=150)
    text = models.TextField('Текст статьи')
    publish_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    #tags =


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


    def __str__(self):
        return self.title