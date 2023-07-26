from django.db import models
from django.urls import reverse

class medicine(models.Model):
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    no_of_pack=models.IntegerField()
    exp=models.DateField()
    list={
        ('i','in_stock'),
        ('o','outof_stock'),
    }
    status=models.CharField(max_length=1,choices=list,default='i')

    def __str__(self):
        return self.title

