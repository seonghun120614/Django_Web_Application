import datetime


from django.db import models
from django.utils import timezone


class Question(models.Model) :

    def __str__(self) :
        return self.question

    def was_published_recently(self) :
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    question = models.CharField(max_length = 100)
    pub_date = models.DateTimeField("date published")



class Choice(models.Model) :

    def __str__(self) :
        return self.answer
    
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer = models.CharField(max_length = 200)
    vote = models.IntegerField(default = 0)