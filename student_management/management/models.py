from django.db import models

class Department(models.Model):
    Did = models.IntegerField(primary_key=True)
    Dname = models.CharField(max_length=100)

    def __str__(self):
        return self.Dname

class Student(models.Model):
    roll_no = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cgpa = models.FloatField()
    marksheet = models.FileField(upload_to='marksheets/')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
