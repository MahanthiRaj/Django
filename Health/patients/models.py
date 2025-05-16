from django.db import models

#object realational mapping(this the pattern)
#every values will map to object automatically 
class patients(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)

class doctors(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)

# Create your models here.
