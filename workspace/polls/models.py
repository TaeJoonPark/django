from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.question_text
        
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.choice_text
        
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    content = models.TextField()
    nowDate = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
# Create your models here.
