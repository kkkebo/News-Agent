from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('register/', SignUp.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    # path('test/', test, name='test'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsCategory.as_view(), name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]
