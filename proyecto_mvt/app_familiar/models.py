from django.db import models    

class Familiar(models.Model):
    name = models.CharField(max_length=64)
    dni = models.IntegerField()
    date_of_birth = models.DateField()