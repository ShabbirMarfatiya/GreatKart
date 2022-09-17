from logging import error
from rest_framework import serializers
from store.models import Product
from category.models import Category
from accounts.models import Account
from rest_framework.authtoken.models import Token

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'slug', 'description', 'price', 'images', 'stock', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'slug', 'description', 'cat_image']

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key', 'user', 'created']

class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match!'})
        account.set_password(password)
        account.save()
        return account