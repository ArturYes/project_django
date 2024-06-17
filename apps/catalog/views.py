from django.shortcuts import render

from apps.catalog.models import Product


def index(request):
    context = {'title': 'Каталог'}

    data = {'objects_list': Product.objects.all()}
    context.update(data)

    return render(request, 'catalog/catalog.html', context)


def contacts(request):
    context = {'title': 'Каталог'}
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}, Номер: {phone}, Сообщение: {message}')
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    context = {
        'title': 'Продукт',
        'object': Product.objects.get(pk=pk)
    }

    return render(request, 'catalog/product.html', context)

