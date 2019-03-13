from django import forms
from django.core.exceptions import ValidationError
from .models import Tag

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