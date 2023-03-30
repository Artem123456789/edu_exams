from django.urls import path
from .views.auth_views import register

app_name = "_auth"

urlpatterns = [
    path("register/", register)
]
