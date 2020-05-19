from django.shortcuts import render
from django.http import HttpResponse

from .models import Article


def home(request):
    article = Article.objects.order_by('-created_at')
    context = {
        'article': article,
        'title': 'Список статей'
    }
    return render(request, 'shop/index.html', context)


def shop(request):
    return HttpResponse('<h1>This is the shop</h1>')
