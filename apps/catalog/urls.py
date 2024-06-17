
from django.urls import path

from apps.catalog.apps import CatalogConfig
from apps.catalog.views import index, contacts, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='catalog'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product')
]
