from django.urls import path

from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('', home, name='home'),
    path('', HomeArticle.as_view(), name='home'),
    path('category/<int:category_id>/', ArticleByCategory.as_view(), name='category'),
    path('article/<int:pk>/', ViewArticle.as_view(), name='view_article'),
    # path('shop/add-article', add_article, name='add_article'),
    path('shop/add-article', CreateArticle.as_view(), name='add_article'),

]
