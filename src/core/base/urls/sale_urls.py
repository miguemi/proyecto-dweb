from core.base.views.sale.views import SaleCreateView,SaleListView,SaleDeleteView, SaleUpdateView, SaleInvoicePdfView
from django.urls import path

app_name = 'sales'

urlpatterns = [
    path('add/', SaleCreateView.as_view(), name="sale_create"),
    path('list/', SaleListView.as_view(), name="sale_list"),
    path('delete/<int:pk>', SaleDeleteView.as_view(), name="sale_delete"),
    path('edit/<int:pk>', SaleUpdateView.as_view(), name="sale_edit"),
    path('invoice/pdf/<int:pk>', SaleInvoicePdfView.as_view(), name="sale_invoice")
]
