from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.blog.forms import ArticleForm
from apps.blog.models import Article


class ArticleListView(ListView):
    model = Article
    extra_context = {'title': 'Статьи'}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = Article.objects.filter(is_publication=True)
        return queryset


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    extra_context = {'title': 'Статья'}
    login_url = reverse_lazy('users:login')

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.count_views += 1
        self.object.save()
        return self.object


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    extra_context = {"title": "Создание статьи"}
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    extra_context = {"title": "Редактирование статьи"}
    login_url = reverse_lazy('users:login')
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.object.slug})


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    fields = ('title', 'text', 'image', 'is_publication',)
    extra_context = {"title": "Удаление статьи"}
    login_url = reverse_lazy('users:login')

    def get_success_url(self):
        return reverse('blog:article_list')
