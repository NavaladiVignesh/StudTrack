from django.db import models
import random

class Student(models.Model):
    studentId = models.IntegerField(max_length=4)
    studentName = models.CharField(max_length=100)
    studentEmail = models.EmailField()
    studentContact = models.IntegerField(max_length=10)
    



