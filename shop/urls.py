from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop),
    path('category/<int:category_id>/', get_category, name='category'),
]
