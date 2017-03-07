from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date publishde")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
# Create your models here.
