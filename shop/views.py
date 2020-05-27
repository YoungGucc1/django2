from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, Category


def home(request):
    article = Article.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'article': article,
        'title': 'Список статей',
        'categories': categories,
    }
    return render(request, 'shop/index.html', context)


def shop(request):
    return HttpResponse('<h1>This is the shop</h1>')


def get_category(request, category_id):
    article = Article.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'shop/category.html', {'article': article, 'categories': categories, 'category': category})

