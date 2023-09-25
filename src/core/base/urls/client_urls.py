from django.urls import path

from core.base.views.client.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = 'client'

urlpatterns = [
    path('list/', ClientListView.as_view(), name='cl_list'),
    path('add/', ClientCreateView.as_view(), name="cl_create"),
    path('edit/<int:pk>', ClientUpdateView.as_view(), name="cl_edit"),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name="cl_delete")
]
