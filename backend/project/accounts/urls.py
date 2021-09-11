from django.urls import path

from accounts.views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    path(r'v1/accounts/registration/', RegistrationAPIView.as_view(), name='user_registration'),
    path(r'v1/accounts/login/', LoginAPIView.as_view(), name='user_login'),
]
