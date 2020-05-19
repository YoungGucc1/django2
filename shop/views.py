from django.shortcuts import render
from django.http import HttpResponse

from .models import Article


def home(request):
    article = Article.objects.all()
    res = '<h1>Список Новостей</h1>'
    for item in article:
        res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    return HttpResponse(res)

def shop(request):
    return HttpResponse('<h1>This is the shop</h1>')
