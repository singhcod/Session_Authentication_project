from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    salary = models.FloatField()
    address = models.CharField(max_length=300)


    def __str__(self):
        return self.ename