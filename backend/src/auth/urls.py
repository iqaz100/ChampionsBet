from django.contrib import admin
from django.urls import path
from .views import LoginAPIView, RegisterAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
]
