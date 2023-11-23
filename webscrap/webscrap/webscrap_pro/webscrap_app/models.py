from django.db import models

# Create your models here.
class weblink(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    lin = models.CharField(max_length=250, null=True, blank=True)