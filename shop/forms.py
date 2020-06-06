from django import forms
from .models import Category
import re
from django.core.exceptions import ValidationError


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5
    }))
    is_published = forms.BooleanField(label='Опубликовано', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
                                      empty_label='Выберите Категорию', widget=forms.Select(attrs={
                                        'class': 'form-control'}))

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название должно называться с цифры')
        return title
