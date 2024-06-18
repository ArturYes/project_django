from django import forms

from apps.blog.models import Article


class StyleForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ArticleForm(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'text', 'image', 'is_publication')

