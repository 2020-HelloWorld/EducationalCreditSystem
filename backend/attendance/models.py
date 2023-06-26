from django.db import models
from home.models import faculty,student,subject


# Create your models here.
class fam(models.Model):
    faculty = models.ForeignKey(faculty,on_delete=models.CASCADE)
    student = models.ForeignKey(student,on_delete=models.CASCADE)
    class Meta:
        unique_together = (('faculty','student'),)
        
class studentcourse(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(student,on_delete=models.CASCADE)
    subject = models.ForeignKey(subject,on_delete=models.CASCADE)
    sem = models.IntegerField()
    attendance = models.FloatField()
    
class declaration(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(student,on_delete=models.CASCADE)
    signed = models.IntegerField()
    doc = models.ImageField(upload_to="uploads")
    
class attendaceRequest(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(student,on_delete=models.CASCADE)
    signed = models.IntegerField()
    
class subjectAttendaceRequest(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(subject,on_delete=models.CASCADE)
    form = models.ForeignKey(attendaceRequest,related_name="subjectRequest",on_delete=models.CASCADE)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()