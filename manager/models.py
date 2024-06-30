from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_uid = models.CharField(max_length=10, primary_key=True)
    employee_name=models.CharField(max_length=100)
    # image=models.ImageField(upload_to="manager/images")
    def __str__(self):
        return self.employee_name

class Leave(models.Model):
    leave_name=models.CharField(max_length=20, primary_key=True)
    leave_color=models.CharField(max_length=10) 
    leave_alias=models.CharField(max_length=5,default='ALS')
    def __str__(self):
        return self.leave_name