import email
from email import message
import numbers
from unicodedata import name
from django.db import models
from django.utils.html import format_html

# Create your models here.
#Create table
class Contact(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length= 100,null=True)
    message = models.TextField(max_length=450,null=False)
    
    def __str__(self):
        return self.email
    

#create category
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateField(auto_created=True,null=True)
    
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px; border-radius:50%;"   />'.format(self.image))
    
#create post
class Post(models.Model):
    Post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')