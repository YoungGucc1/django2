from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop),
    path('category/<int:category_id>/', get_category, name='category'),
    path('shop/<int:article_id>/', view_article, name='view_article')
]
