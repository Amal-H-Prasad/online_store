from datetime import timezone

from django.db import models

# Create your models here.


class user_login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)

    class Meta:
        db_table = "user_login"


class User_Register(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    class Meta:
        db_table = "User_Register"

class review(models.Model):
    title=models.TextField()
    feedback=models.TextField()
    feeddate=models.DateField(auto_now_add=True)
    username=models.TextField()

    class Meta:
          db_table="review"