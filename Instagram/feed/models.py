from django.db import models
from Instagram import settings


class Post(models.Model):
    matn = models.CharField(max_length=300,blank=True)
    likes = models.ManyToManyField(settings.INSTA_ACCOUNT,related_name="post_like",blank=True)
    def __str__(self):
        return self.matn

class Comment(models.Model):
    matn = models.CharField(max_length=300)
    user = models.ForeignKey(settings.INSTA_ACCOUNT,on_delete=models.CASCADE,related_name="post_comments")
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.INSTA_ACCOUNT,related_name="comment_like",blank=True)
    def __str__(self):
        return self.matn

class Media(models.Model):
    videos = models.URLField(blank=True)
    photos = models.URLField(blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

class Message(models.Model):
    matn = models.CharField(max_length=50, blank=True)
    yuboruvchi = models.ForeignKey(settings.ACC, on_delete=models.CASCADE, related_name="message_yuboruvchi")
    qabul = models.ForeignKey(settings.ACC, on_delete=models.CASCADE, related_name="message_qabul")
    vaqt = models.DateTimeField(auto_now_add=True)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100, blank=True)
def __str__(self):
    return '%s' % (self.name)

