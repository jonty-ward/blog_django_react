from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=100)
    subTopic = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.title} - {self.topic} "