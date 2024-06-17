from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.blog.models import Article


class ArticleListView(ListView):
    model = Article
    extra_context = {'title': 'Статьи'}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = Article.objects.filter(is_publication=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article
    extra_context = {'title': 'Статья'}

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.count_views += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'text', 'image', 'is_publication',)
    extra_context = {"title": "Создание статьи"}

    def get_success_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.object.slug})


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'text', 'image', 'is_publication',)
    extra_context = {"title": "Редактирование статьи"}

    def get_success_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.object.slug})


class ArticleDeleteView(DeleteView):
    model = Article
    fields = ('title', 'text', 'image', 'is_publication',)
    extra_context = {"title": "Удаление статьи"}

    def get_success_url(self):
        return reverse('blog:article_list')
