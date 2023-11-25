from django.db import models

# Create your models here.
class crimereport(models.Model):
   incidenttype =models.CharField(max_length=50)
   description=models.CharField(max_length=1000)
   yourcontactinformation =models.IntegerField()
   location=models.CharField(max_length=100)
   
   def __str__(self):
      return self.location