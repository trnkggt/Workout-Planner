from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views


urlpatterns = [
    path("registration/", views.RegistrationView.as_view(),
         name='token_registration'),
    path("login/", TokenObtainPairView.as_view(),
         name='token_login'),
    path("logout/", views.UserLogOut.as_view(),
         name='token_logout')
]