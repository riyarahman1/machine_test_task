from django.urls import path
from usertask .views import *

urlpatterns = [
    path('taskcreate',Taskcreate.as_view(),name='taskcreate'),
    path('tasklist',Tasklist.as_view(),name='tasklist'),
    path('taskcompletedlist',Taskcompletedlist.as_view(),name='taskcompletedlist'),
    path('tasknotcompletedlist',Tasknotcompletedlist.as_view(),name='tasknotcompletedlist'),
    path('usertasklist/<int:id>/',Usertasklist.as_view(),name='usertasklist'),
    path('usersort',Usersort.as_view(),name='usersort'),
    path('taskupdated/<int:id>/',TaskUpdated.as_view(),name='taskupdated'),




]