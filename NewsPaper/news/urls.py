from django.urls import path

from .views import (NewsList, NewsDetail, NewsListSearch, PostCreate, PostUpdate,
                    PostDelete, PostCreateAR, PostUpdateAR, PostDeleteAR)

urlpatterns = [
    path('', NewsList.as_view(), name='all_news'),
    path('<int:pk>', NewsDetail.as_view(), name='detail_one_news'),
    path('search', NewsListSearch.as_view(), name='news_search'),
    path('news/create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/news/edit/', PostUpdate.as_view(), name='news_create'),
    path('<int:pk>/news/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/create/', PostCreateAR.as_view(), name='articles_create'),
    path('<int:pk>/articles/edit/', PostUpdateAR.as_view(), name='articles_create'),
    path('<int:pk>/articles/delete/', PostDeleteAR.as_view(), name='articles_delete'),
]