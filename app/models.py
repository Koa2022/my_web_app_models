from django.db import models

# Create your models here.

PREFIX = (
    (1, "นาย"),
    (2, "นางสาว"),
    (3, "นาง")
)


class Student(models.Model):
    
    prefix = models.IntegerField(choices=PREFIX)
    
    std_id = models.IntegerField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    
    phone = models.CharField(max_length=10)
    
    