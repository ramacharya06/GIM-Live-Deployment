from django.db import models

# Create your models here.
class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    votes = models.IntegerField(default=0)

class IPs(models.Model):
    id = models.AutoField(primary_key=True)
    ip_address = models.GenericIPAddressField(unique=True)
