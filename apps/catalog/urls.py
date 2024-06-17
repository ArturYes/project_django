
from django.urls import path

from apps.catalog.apps import CatalogConfig
from apps.catalog.views import index, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts')
]