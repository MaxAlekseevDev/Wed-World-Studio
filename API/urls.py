from django.urls import path
from .views import UserApiController

api_name = "API"

urlpatterns = [
    path('users', UserApiController),
]