from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to="files")

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.name