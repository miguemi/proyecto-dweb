from django.forms import ModelForm

from core.base.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
