from django.urls import path

from core.base.views.category.views import CategoryListView, CategoryCreateView


app_name = 'category'

urlpatterns = [
    path('list/', CategoryListView.as_view(), name='cat_list'),
    path('add/', CategoryCreateView.as_view(), name="cat_create")
]
