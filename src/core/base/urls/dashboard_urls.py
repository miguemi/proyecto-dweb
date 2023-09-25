from django.urls import path

from core.base.views.dashboard.views import DashboardView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name="main")
]
