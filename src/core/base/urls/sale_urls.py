from core.base.views.sale.views import SaleCreateView,SaleListView,SaleDeleteView
from django.urls import path

app_name = 'sales'

urlpatterns = [
    path('add/', SaleCreateView.as_view(), name="sale_create"),
    path('list/', SaleListView.as_view(), name="sale_list"),
    path('delete/<int:pk>', SaleDeleteView.as_view(), name="sale_delete")
]
