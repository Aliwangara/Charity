from django.db import models

# Create your models here.

import os.path
import uuid

from django.db import models

# for unique image if no image exists in a volunteers description
def unique_img_name(instance, filename):
    name = uuid.uuid4()
    print(name)
    ext = filename.split(".")[-1]
    full_name = f"{name}. {ext}"
    full_name = "%s.%s" %(name, ext)
    return os.path.join('volunteers', full_name)
# Create your models here.


# volunteers data 
class Volunteers(models.Model):
    #     name, Email, dob, salary, disable
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=6, decimal_places=1)#67000.58
    disabled = models.BooleanField(default= False)
    profile = models.ImageField(upload_to=unique_img_name, null=True ,default = 'employees/employee.png' )
    created_at = models.DateTimeField(auto_now_add=True, null=True)#once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True)#every time an update happens
    
    def __str__ (self):
       return self.name

# contact form data
class Contacts(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=20)
    subject  = models.TextField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.name

# Data for things we have done so far 
class cause(models.Model):
    Title= models.CharField(max_length=40)
    profile= models.ImageField(upload_to='upload/cause')
    summary = models.CharField(max_length=5000)
    
    def __str__(self):
        return self.Title
    
    
    
# Data about oncoming events
class Event(models.Model):
    name = models.CharField(max_length=50)
    profile= models.ImageField(upload_to='upload/Events')
    About =models.CharField(max_length=50)
    subject = models.CharField(max_length=250)
    # Link = models.URLField( max_length=150, unique=True, blank=True)
    Date = models.DateField(auto_now=True, null= True)
    is_new = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    # for changing number of donations you have done
class Number(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    # testimonials Data
class happy_customers(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True, upload_to='upload/happy_customers')
    position = models.CharField(max_length=10)
    information =models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    
    
class Volunteer_application(models.Model):
        name = models.CharField(max_length=20)
        Email = models.EmailField(max_length=30)
        subject =models.CharField(max_length=20)
        post = models.FileField(upload_to='upload/Volunteer_form', null=True)
        comment = models.CharField(null=True, max_length=400)
        
        def __str__(self):
            return self.name