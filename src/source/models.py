from django.db import models

# Create your models here.


class Topic(models.Model):

    name = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to="topic_images/", default="topic_images/default_topic_images.png")

    def __str__(self):
        return f'Topic: {self.name}'


class Source(models.Model):

    title = models.CharField(max_length=25, null=False)
    description = models.TextField(max_length=255, null=False)
    image = models.ImageField(upload_to="source_images/", default="source_images/default_source_images.png")

    def __str__(self):
        return f'Title: {self.title}, Description: {self.description}'

    class Meta:
        ordering = ['title']


class Information(models.Model):

    text = models.TextField(max_length=3000, null=False)

    def __str__(self):
        return f'Text: {self.text}'
