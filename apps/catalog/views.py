from django.views.generic import ListView, DetailView, TemplateView

from apps.catalog.models import Product


class ProductListView(ListView):
    template_name = 'catalog/product_list.html'
    model = Product
    extra_context = {'title': 'Каталог'}


class ProductDetailView(DetailView):
    template_name = 'catalog/product_detail.html'
    model = Product


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
