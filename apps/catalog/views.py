from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView, DeleteView

from apps.catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from apps.catalog.models import Product, Version, Category
from apps.catalog.services import get_categories_from_cache, get_products_from_cache


class ProductListView(ListView):
    template_name = 'catalog/product_list.html'
    model = Product
    extra_context = {'title': 'Каталог товаров'}

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('users:login')
    template_name = 'catalog/product_detail.html'
    model = Product
    extra_context = {"title": "Просмотр товара"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        active_version = Version.objects.filter(product=product, is_active=True).first()
        context['active_version'] = active_version
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    model = Product
    extra_context = {"title": "Редактирование товара"}

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return ProductForm
        elif user.has_perms([
            'catalog.can_change_category',
            'catalog.can_change_description',
            'catalog.set_published_status'
        ]):
            return ModeratorProductForm

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if (user != self.get_object().owner and not user.is_superuser and
                not user.groups.filter(name='Moderator').exists()):
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:login')
    model = Product
    form_class = ProductForm
    extra_context = {"title": "Создание товара"}
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['objects_list'] = Category.objects.all()
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            self.object.owner = self.request.user
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users:login')
    model = Product
    extra_context = {"title": "Удаление товара"}
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user != self.get_object().owner and not user.is_superuser:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {'title': 'Контакты'}

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}, Номер: {phone}, Сообщение: {message}')
        return self.render_to_response(context)


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'

    def get_queryset(self):
        return get_categories_from_cache()


class CategoryDetailView(ListView):
    model = Product
    template_name = 'catalog/category_detail.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(category=self.kwargs.get('pk'))
        return queryset
