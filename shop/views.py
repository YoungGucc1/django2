from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Article, Category
from .forms import ArticleForm


class HomeArticle (ListView):
    model = Article
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('category')


class ArticleByCategory(ListView):
    model = Article
    context_object_name = 'article'
    allow_empty = False

    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewArticle(DetailView):
    model = Article
    context_object_name = 'article_item'


class CreateArticle(CreateView):
    form_class = ArticleForm
    template_name = 'shop/add_article.html'


# def home(request):
#     article = Article.objects.order_by('-created_at')
#     context = {
#         'article': article,
#         'title': 'Список статей',
#
#     }
#     return render(request, 'shop/index.html', context)


# def get_category(request, category_id):
#     article = Article.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'shop/category.html', {'article': article, 'category': category})


# def view_article(request, article_id):
#     # article_item = Article.objects.get(pk=article_id)
#     article_item = get_object_or_404(Article, pk=article_id)
#
#     return render(request, 'shop/view_article.html', {"article_item": article_item})


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            article = Article.objects.create(**form.cleaned_data)
            return redirect(article)
    else:
        form = ArticleForm()
    return render(request, 'shop/add_article.html', {'form': form})
#
#
# def shop(request):
#     return HttpResponse('<h1>This is the shop</h1>')