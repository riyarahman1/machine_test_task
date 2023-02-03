from rest_framework import serializers
from .models import Task
from application.serializers import *



class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class Tasklistserializer(serializers.ModelSerializer):
    Assigned_To = UserdetailsSerializer()
    class Meta:
        model = Task
        fields = '__all__'

