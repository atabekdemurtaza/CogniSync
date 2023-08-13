from rest_framework import serializers
from orbit.models import Product, Category
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    modules = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'name',
            'isAdmin',
            'email',
            'first_name',
            'last_name',
            'date_joined'
        ]

    def get_name(self, obj):
        name = obj.first_name
        if name == "":
            name = obj.email
        return name

    def get_isAdmin(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'name',
            'isAdmin',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'token',
        ]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)
