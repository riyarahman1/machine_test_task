from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    
class Listuser(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    