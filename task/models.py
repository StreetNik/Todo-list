from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    content = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")
