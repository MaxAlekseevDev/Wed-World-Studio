from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from .serializer import UserSerializer, ProfileSerializer

# Create your views here.
class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def get(self, request):
        return Response()

    def post(self, request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            User.objects.create(**serialized.data)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)