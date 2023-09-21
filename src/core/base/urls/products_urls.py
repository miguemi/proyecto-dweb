from core.base.views.product.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='prod_list'),
    path('add/', ProductCreateView.as_view(), name="prod_create"),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name="prod_edit"),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name="prod_delete"),
]
