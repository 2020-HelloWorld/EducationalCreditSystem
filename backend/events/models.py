from django.db import models
from home.models import club,student

# Create your models here.

class event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    date = models.DateField()
    club = models.ForeignKey(club,on_delete=models.CASCADE)
    details =  models.CharField(max_length=1000)

class participant(models.Model):
    id = models.AutoField(primary_key=True)
    srn = models.ForeignKey(student,on_delete=models.CASCADE)
    event = models.ForeignKey(event,on_delete=models.CASCADE)
    
class winner(models.Model):
    id = models.OneToOneField(participant,primary_key=True,on_delete=models.CASCADE)
    position = models.IntegerField(null=False)
    
class image(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="uploads")

class organizer(models.Model):
    id = models.AutoField(primary_key=True)
    srn = models.ForeignKey(student,on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    event = models.ForeignKey(event,on_delete=models.CASCADE)  

    
    
    
    