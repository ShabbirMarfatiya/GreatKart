from django.shortcuts import render
from rest_framework import response
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from store.models import Product
from rest_framework import generics, permissions, mixins, serializers, status
from .serializers import ProductSerializer, CategorySerializer, RegistrationSerializer, TokenSerializer
from rest_framework.response import Response
from category.models import Category
from accounts.models import Account
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

def home(request):
    products = Product.objects.all().filter(is_available=True)
    return render(request, 'home.html', {'products': products})

def add(a,b):
    sum = a+b
    return sum

def sub(a, b):
    add = a + b
    return add

def mul(a,b):
    m = a*b
    return m

def sub(a,b):
    s = a-b
    retunr s

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

class TokenList(generics.ListCreateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
