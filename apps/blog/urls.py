from django.urls import path

from apps.blog.apps import BlogConfig
from apps.blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('articles', ArticleListView.as_view(), name='article_list'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/update/<str:slug>/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<str:slug>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<str:slug>/', ArticleDetailView.as_view(), name='article_detail'),
]
