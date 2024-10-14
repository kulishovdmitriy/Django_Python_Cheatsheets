from django.db import models

# Create your models here.


class Topic(models.Model):

    name = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to="topic_images/", default="topic_images/default_topic_images.png")

    def __str__(self):
        return f'{self.name}'


class Source(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='sources')
    title = models.CharField(max_length=25, null=False)
    description = models.TextField(max_length=255, null=False)
    image = models.ImageField(upload_to="source_images/", default="source_images/default_source_images.png")

    def __str__(self):
        return f'{self.title}, {self.description}'

    class Meta:
        ordering = ['title']


class Information(models.Model):

    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='information')
    text = models.TextField(max_length=8000, null=False, blank=True)

    def __str__(self):
        return f'{self.text}'
