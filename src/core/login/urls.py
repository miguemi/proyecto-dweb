from django.urls import path

from core.login.views import *

app_name = 'security'

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutRedirectView.as_view(), name='logout'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password')
]
