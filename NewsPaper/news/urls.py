from django.urls import path

from .views import (NewsList, NewsDetail, NewsListSearch, PostCreate, PostUpdate,
                    PostDelete, PostCreateAR, PostUpdateAR, PostDeleteAR, CategoryListView, subscribe, subscriptions)
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60*1)(NewsList.as_view()), name='all_news'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', NewsDetail.as_view(), name='detail_one_news'),
    path('search', NewsListSearch.as_view(), name='news_search'),
    path('news/create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/news/edit/', PostUpdate.as_view(), name='news_create'),
    path('<int:pk>/news/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/create/', PostCreateAR.as_view(), name='articles_create'),
    path('<int:pk>/articles/edit/', PostUpdateAR.as_view(), name='articles_create'),
    path('<int:pk>/articles/delete/', PostDeleteAR.as_view(), name='articles_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscriptions', subscribe, name='subscriber'),
]