from django.urls import path
from .views import CreateUserView

api_name = "API"

urlpatterns = [
    path('users/register', CreateUserView.as_view()),
]