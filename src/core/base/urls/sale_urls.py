from core.base.views.sale.views import SaleCreateView
from django.urls import path

app_name = 'sales'

urlpatterns = [
    path('add/', SaleCreateView.as_view(), name="sale_create"),
]
