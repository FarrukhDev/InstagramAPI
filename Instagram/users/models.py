from django.contrib.auth.models import User
from django.db import models

from Instagram import settings


class Account(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date=models.DateField(blank=True)
    bio=models.CharField(max_length=150,blank=True)
    prof_pic=models.URLField(blank=True)
    gender=models.CharField(max_length=10,choices=(('male','male'),('female','female')))
    followers = models.ForeignKey(settings.INSTA_ACCOUNT,on_delete=models.CASCADE,related_name="user_followers",blank=True)
    following = models.ForeignKey(settings.INSTA_ACCOUNT,on_delete=models.CASCADE,related_name="user_followings",blank=True)
    def __str__(self):
        return f"{self.name},{self.surname}"

    def followers_soni(self):
        return self.followers.count()
    def following_soni(self):
        return self.following.count()

