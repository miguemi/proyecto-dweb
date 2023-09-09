from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from core.base.models import Category

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context