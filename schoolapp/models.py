from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    is_parent  = models.BooleanField('parent status', default=False)
    is_principal = models.BooleanField('principal status', default=False)    


class Principal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    First_Name = models.CharField(max_length=50, default="")
    Last_Name = models.CharField(max_length=50, default="")  
    Email = models.EmailField(default=False,blank=True)  
    Mobile= models.IntegerField(default=0)   
    image = models.ImageField(upload_to='media/images', default="")    
    def __str__(self):
        return self.First_Name + " "+self.Last_Name          

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    FirstName = models.CharField(max_length=50, default="")
    LastName = models.CharField(max_length=50, default="") 
    Email = models.EmailField(default=False,blank=True)  
    Mobile= models.IntegerField(default=0)    
    image = models.ImageField(upload_to='media/images', default="")
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111) 
    Subject=  models.CharField(max_length=50, default="")  
    principal = models.ForeignKey(Principal, on_delete=models.CASCADE) 
    def __str__(self):
        return self.First_Name + " "+self.Last_Name    

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    First_Name = models.CharField(max_length=50, default="")
    Last_Name = models.CharField(max_length=50, default="")   
    Email = models.EmailField(default=False,blank=True)
    Mobile= models.IntegerField(default=0)   
    image = models.ImageField(upload_to='media/images', default="")  
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111) 
    def __str__(self):
        return self.First_Name + " "+self.Last_Name            

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    FirstName = models.CharField(max_length=50, default="")
    LastName = models.CharField(max_length=50, default="")    
    Email = models.EmailField(default=False,blank=True) 
    Mobile= models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/images', default="")
    RollNo= models.IntegerField(default=0)
    Class = models.CharField(max_length=5, default="")  
    Percentage=models.CharField(max_length=50, default="")  
    teacher = models.ManyToManyField(Teacher)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    def __str__(self):
        return self.First_Name + " "+self.Last_Name               

 

    