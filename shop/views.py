from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Article, Category
from .forms import ArticleForm


def home(request):
    article = Article.objects.order_by('-created_at')
    context = {
        'article': article,
        'title': 'Список статей',

    }
    return render(request, 'shop/index.html', context)


def get_category(request, category_id):
    article = Article.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'shop/category.html', {'article': article, 'category': category})


def view_article(request, article_id):
    # article_item = Article.objects.get(pk=article_id)
    article_item = get_object_or_404(Article, pk=article_id)

    return render(request, 'shop/view_article.html', {"article_item": article_item})


def add_article(request):
    if request.method == 'POST':
        pass
    else:
        form = ArticleForm()
    return render(request, 'shop/add_article.html', {'form': form})


def shop(request):
    return HttpResponse('<h1>This is the shop</h1>')