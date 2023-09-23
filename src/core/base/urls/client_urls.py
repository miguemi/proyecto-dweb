from django.urls import path

from core.base.views.client.views import ClientView

app_name = 'client'

urlpatterns = [
    path('', ClientView.as_view(), name='cl_list'),
]
