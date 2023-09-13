from django.urls import path

from core.base.views.category.views import CategoryListView, CategoryCreateView, CategoryUpdateView


app_name = 'category'

urlpatterns = [
    path('list/', CategoryListView.as_view(), name='cat_list'),
    path('add/', CategoryCreateView.as_view(), name="cat_create"),
    path('edit/<int:pk>', CategoryUpdateView.as_view(), name="cat_edit")
]
