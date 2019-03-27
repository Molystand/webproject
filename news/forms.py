from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, News, Comment


class TagForm(forms.ModelForm):
    class Meta:
        # Поля для формы (из модели)
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            # Стили для полей виджета (формы)
            'title': forms.TextInput(attrs={'class': 'myclass'}),
            'slug': forms.TextInput(attrs={'class': 'myclass'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug не может иметь значение "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug не уникален. Уже есть slug "{}"'.format(new_slug))
        return new_slug


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'slug', 'text_preview', 'text', 'tags']

        widgets = {
            # 'user': forms.Select(attrs={'class': 'myclass'}),
            'title': forms.TextInput(attrs={'class': 'myclass'}),
            'slug': forms.TextInput(attrs={'class': 'myclass'}),
            'text_preview': forms.Textarea(attrs={'class': 'myclass'}),
            # 'picture_preview_path': forms.TextInput(attrs={'class': 'myclass'}),
            'text': forms.Textarea(attrs={'class': 'myclass'}),
            'tags': forms.SelectMultiple(attrs={'class': 'myclass'})
        }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('Slug не может иметь значение "Create"')
            return new_slug


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'user': forms.Textarea(attrs={'class': 'myclass'})
        }
