from django.utils import timezone
from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=100,null=True)
    task_content = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now,null=True)
    complete = models.BooleanField(default=False,null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True)
    image2 = models.ImageField(upload_to='images2',null=True)  


    def __str__(self):
        return self.title




class Name(models.Model):
    name = models.CharField(max_length=100,null=True)
    

    def __str__(self):
        return self.name

class Persons(models.Model):
 
    name = models.ForeignKey(Name, on_delete=models.CASCADE,null=True,unique=True)


    def __str__(self):
        return self.name.name





class students(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now,null=True)


    def __str__(self):
        return self.name





class Owner(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.TextField(null=True)
    gender = models.DateTimeField(default=timezone.now,null=True)
   


    def __str__(self):
        return self.name

class House(models.Model):
    name = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='images',null=True)  

    floors = models.CharField(max_length=100,null=True)
    carpetarea = models.CharField(max_length=100,null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,null=True)


    

    def __str__(self):
        return self.name


class createuser(models.Model):
    username = models.CharField(max_length=100,null=True,unique=True)
    password = models.CharField(max_length=100,null=True)

   


    def __str__(self):
        return self.username



#################################################################################################BLOG######################################

class Blogger(models.Model):
    username = models.CharField(max_length=100,null=True,unique=True)
    password = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.username


class blog(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    blogger_name = models.ForeignKey(Blogger, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title