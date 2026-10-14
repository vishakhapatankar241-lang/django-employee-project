from django.db import models

# Create your models here.

class Employee(models.Model):
    id =models.AutoField(primary_key=True)
    employee_code=models.CharField(max_length=20,unique=True) 
    employee_name=models.CharField(max_length=100) 
    email=models.EmailField (unique=True)
    mobile=models.CharField(max_length=10)
    technology=models.CharField(max_length=50) 
    experience=models.DecimalField(max_digits=4 ,decimal_places=1)  
    city=models.CharField(max_length=50)  
    salary= models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=20,choices=[('Active','Active'),('Inactive','Inactive')]) 
    
    class Meta:
        db_table = "employee"
        ordering = ["employee_name"]

    def __str__(self):
        return f"{self.employee_name} ({self.technology})"