from django.urls import path

from core.base.views.category.views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from core.base.views.dashboard.views import DashboardView

app_name = 'category'

urlpatterns = [
    path('list/', CategoryListView.as_view(), name='cat_list'),
    path('add/', CategoryCreateView.as_view(), name="cat_create"),
    path('edit/<int:pk>', CategoryUpdateView.as_view(), name="cat_edit"),
    path('delete/<int:pk>', CategoryDeleteView.as_view(), name="cat_delete"),
    path('', DashboardView.as_view(), name="dashboard")
]
