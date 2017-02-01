from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

class OpenSrcProject(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    num_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.project_name

class Comment(models.Model):
    project = models.ForeignKey(OpenSrcProject, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.comment_text