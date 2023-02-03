from django.shortcuts import render
from django.db.models import Count
from django.db.models import Q
from .models import Task
from .serializers import Taskserializer,Tasklistserializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
# Create your views here.




class Taskcreate(generics.CreateAPIView):
    queryset=Task.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=Taskserializer

class Tasklist(generics.ListAPIView):
    queryset = Task.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=Tasklistserializer
 
class Taskcompletedlist(generics.ListAPIView):
    queryset = Task.objects.filter(Status='done').all()
    permission_classes = (AllowAny,)
    serializer_class=Tasklistserializer 


class Tasknotcompletedlist(generics.ListAPIView):
    queryset = Task.objects.filter(Status='open/notdone').all()
    permission_classes = (AllowAny,)
    serializer_class=Tasklistserializer 

class Usertasklist(APIView):
    def get(self,request,id):
        user = Task.objects.filter(Assigned_To = id).all()
        All = Tasklistserializer(user,many=True)
        return Response(All.data,status=200)

class Usersort(APIView):
    def get(self,request):
        Status=None
        user = User.objects.annotate(task_count=Count('task', filter=Q(Status="done"))).order_by('-task_count')
        All = UserSerializer(user,many=True)
        return Response(All.data,status=200)

class TaskUpdated(APIView):
    def post(self,request,id):
        task = Task.objects.get(id=id)
        task.Status="done"
        task.save()
        return Response(status=200)
    