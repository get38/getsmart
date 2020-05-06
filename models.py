# Create your models here.
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.utils import timezone
from datetime import datetime
from django import template
from django.utils.timesince import timesince
from django.contrib.humanize.templatetags import humanize

class authors(models.Model): 
    username=models.CharField(max_length=50)        
    images=models.ImageField(upload_to='image_author/')
    def __str__(self):
         return self.username        
         
class categorys(models.Model):
    cateoryname=models.CharField(max_length=50)    
    def __str__(self):   
        return self.cateoryname              
    #def get_set(self):
       # return Post.objects.filter(category_id=self.kwargs.get('pk'))
class blogs(models.Model):
    title=models.CharField(max_length=80)
    description=models.TextField(max_length=3000)   
    authors=models.ForeignKey(authors,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image_post/')   
    published_date=models.DateTimeField()          
    published = models.BooleanField(default=True)
    categorys=models.ForeignKey(categorys,on_delete=models.CASCADE)
    def __str__(self):   
        return self.title
   
class Post(models.Model):
    name= models.CharField(max_length=300)
    email= models.EmailField(unique=True)    
    subject=models.TextField(max_length=80)
    message=models.TextField(max_length=100) 
    
class commissoner_message(models.Model):
    image_com=models.ImageField(upload_to='Comm_message/')
    message=models.TextField(max_length=500)
     
class uploader(models.Model):
    title=models.TextField(max_length=30)
    file_pdc=models.FileField(upload_to='pdc_file/')
    uploaded_date=models.DateTimeField()  
    uploaded =models.BooleanField(default=True)
    def __str__(self):
        return self.title 

 
   
class comment(models.Model):           
    name = models.CharField(max_length=45)
    email=models.EmailField()
    message=models.TextField(max_length=100)    
    blogs=models.ForeignKey(blogs,on_delete=models.CASCADE)   
    def __str__(self):
        return self.name
class uploadergetimg(models.Model):
    uploaderimgget = models.ImageField(upload_to='image_upload/') 
    place=models.CharField(max_length=50)
    def __str__(self):
        return self.place

class leaders(models.Model):  
    name=models.CharField(max_length=20) 
    uploaded_img = models.ImageField(upload_to='top_leaders/')  
    postion=models.CharField(max_length=20)

    def __str__(self):
       return self.name
class vacancy(models.Model):
    postion=models.CharField(max_length=45)
    place=models.CharField(max_length=20)
    qualification=models.TextField(max_length=900)

class resource_uploader(models.Model):
    title_reso=models.CharField(max_length=30)
    des=models.TextField(max_length=500) 
    file_pdc_re=models.FileField(upload_to='pdc_res/')
    uploaded_date=models.DateTimeField()  
    uploaded =models.BooleanField(default=True)
    
    def __str__(self):
        return self.title_reso 
class planning_uploader(models.Model):
    title_planning=models.CharField(max_length=30)
    desc=models.TextField(max_length=500) 
    file_pdc_pl=models.FileField(upload_to='pdc_planning/')
    uploaded_date=models.DateTimeField()            
    uploaded =models.BooleanField(default=True)
    
    def __str__(self):
        return self.title_planning 

class reports_uploader(models.Model):
    title_report=models.CharField(max_length=30)
    desc_repo=models.TextField(max_length=500) 
    file_pdc_report=models.FileField(upload_to='pdc_report/')
    uploaded_date=models.DateTimeField()  
    uploaded =models.BooleanField(default=True)
    
    def __str__(self):
        return self.title_report         


class guidelines_uploader(models.Model):
    title_guide=models.CharField(max_length=30)
    desc_guide=models.TextField(max_length=500) 
    file_pdc_guide=models.FileField(upload_to='pdc_guide/')
    uploaded_date=models.DateTimeField()  
    uploaded =models.BooleanField(default=True)
    
    def __str__(self):
        return self.title_guide


class rule_uploader(models.Model):
    title_rule=models.CharField(max_length=30)
    desc_rule=models.TextField(max_length=500) 
    file_pdc_rule=models.FileField(upload_to='pdc_guide/')
    uploaded_date=models.DateTimeField()  
    uploaded =models.BooleanField(default=True)
    
    def __str__(self):
        return self.title_rule


class videup(models.Model):
    videofile=models.FileField(upload_to='pdc_guide/')
    









    
    