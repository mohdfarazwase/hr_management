from django.db import models

# Create your models here.


class Profile(models.Model):
    gender_choices = [
        ('male' , "Male"),
        ('female' , "Female"),
        ('other' , "Dont want to disclose")
    ]
    first_name = models.CharField(max_Length=50)
    last_name = models.CharField(max_Length=50)
    picture= models.ImageField(upload_to='profile/')
    gender = models.CharField(max_Length=10 , choices= gender_choices)
    bio = models.TextField()


    