from django import forms
from django.forms import BooleanField

from apps.catalog.models import Version, Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        exclude = ('product',)


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'owner')

    def clean_name(self):
        clean_name = self.cleaned_data['name']
        words_from_title = clean_name.lower().split()
        for forbidden_word in self.forbidden_words:
            for word in words_from_title:
                if forbidden_word == word:
                    raise forms.ValidationError(f'Название продукта не может содержать слово "{forbidden_word}"')
        return clean_name

    def clean_description(self):
        clean_description = self.cleaned_data['description']
        words_from_description = clean_description.lower().split()
        for forbidden_word in self.forbidden_words:
            for word in words_from_description:
                if forbidden_word == word:
                    raise forms.ValidationError(f'Описание продукта не может содержать слово "{forbidden_word}"')
        return clean_description


class ModeratorProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'is_published', 'category')
