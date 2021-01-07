import datetime

from django.db import models

# Create your models here.
class register(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    dob=models.DateField(default=datetime.date.today)
    address=models.TextField(max_length=500)
    qual=models.CharField(max_length=100)
    mob=models.IntegerField()
    pname=models.CharField(max_length=100)
    pmob=models.IntegerField()
    email=models.EmailField()
    img=models.ImageField(upload_to='image')
    course=models.CharField(max_length=500)