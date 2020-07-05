from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, User


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'email')
        model = get_user_model()
