from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from apps.catalog.apps import CatalogConfig
from apps.catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryDetailView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', cache_page(60)(ContactsView.as_view()), name='contacts'),
    path('product/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/update/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('product/delete/<int:pk>/', never_cache(ProductDeleteView.as_view()), name='product_delete'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]
