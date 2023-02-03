from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    STATUS = (
        ('open/notdone','open/notdone'),
        ('done','done'),
    )
    Title = models.CharField(max_length=255)
    Description = models.TextField(max_length=255)
    Status = models.CharField(max_length=100,choices=STATUS,default="open/notdone")
    Assigned_To = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="task")
    Date = models.DateField(auto_now_add=True)

