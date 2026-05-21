from django.urls import path
from users.views import UserRegisterView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from users.views import SimpleJWTView
from users.oauth_2 import GoogleLoginOauth

urlpatterns = [
    path("registration/", UserRegisterView.as_view()),
    path('api/token/', SimpleJWTView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('google_login/', GoogleLoginOauth.as_view()),
]