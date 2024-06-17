from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта")
    image = models.ImageField(upload_to='catalog/product/', default='catalog/product/default_logo_product.png',
                                                                    **NULLABLE, verbose_name="Фото продукта")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.PositiveIntegerField(verbose_name='Цена продукта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name} - {self.price} руб.'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
