from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Profile

class UserSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = User
        fields = ['password','username', 'first_name', 'last_name', 'email']
        write_only_fields = ('password',)

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

    