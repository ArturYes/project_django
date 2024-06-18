from django.urls import path
from django.views.decorators.cache import never_cache

from apps.blog.apps import BlogConfig
from apps.blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('articles', ArticleListView.as_view(), name='article_list'),
    path('article/create/', never_cache(ArticleCreateView.as_view()), name='article_create'),
    path('article/update/<str:slug>/', never_cache(ArticleUpdateView.as_view()), name='article_update'),
    path('article/delete/<str:slug>/', never_cache(ArticleDeleteView.as_view()), name='article_delete'),
    path('article/<str:slug>/', ArticleDetailView.as_view(), name='article_detail'),
]
