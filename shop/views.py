from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article, Category
from .forms import ArticleForm, UserRegisterForm, UserLoginForm, ContactForm

from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'shop/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'shop/register.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'gucc1y@yandex.kz', ['dilfar41@gmail.com'], fail_silently=True)
            messages.success(request, 'Вы успешно зарегистрировались')
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('test')
            else:
                messages.error(request, 'Ошибка отправки')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = ContactForm()
    return render(request, 'shop/test.html')




class HomeArticle (ListView):
    model = Article
    context_object_name = 'article'
    paginate_by = 20

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


class CreateArticle(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = 'shop/add_article.html'
    # login_url = '/admin/'
    login_url = reverse_lazy('home')





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


# def add_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             article = Article.objects.create(**form.cleaned_data)
#             return redirect(article)
#     else:
#         form = ArticleForm()
#     return render(request, 'shop/add_article.html', {'form': form})


#
#
# def shop(request):
#     return HttpResponse('<h1>This is the shop</h1>')