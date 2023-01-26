from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from . import views

urlpatterns = [
    path('gender/users', views.UserGenderStatisticView.as_view()),
    path('age/users', views.UserAgeStatisticView.as_view()),
    path('gender/boards', views.BoardGenderStatisticView.as_view()),
    path('age/boards', views.BoardAgeStatisticView.as_view()),
]