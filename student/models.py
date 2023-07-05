from django.db import models

class Department(models.Model):
    studentDepartment = models.CharField(max_length=5)

class Student(models.Model):
    studentId = models.IntegerField(max_length=4)
    studentName = models.CharField(max_length=100)
    studentEmail = models.EmailField()
    studentContact = models.IntegerField(max_length=10)
    studentDepartment = models.ForeignKey(Department,on_delete=models.CASCADE)



