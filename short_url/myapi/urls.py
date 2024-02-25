from django.contrib import admin
from django.urls import path

from .views import TokenApiView

app_name = 'api'


urlpatterns = [
    path('token/', TokenApiView.as_view()),
]
