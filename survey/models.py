import datetime

from django.db import models
from django.utils import timezone

# Djang는 1:1 n:1 1:n의 데이터베이스 관계들을 지원

class Question(models.Model) :
    
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self) :
        return self.question_text
    
    def was_published_recently(self) :
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model) :

    # 👇🏻 ForeignKey는 각각의 Choice가 하나의 Question에 관계된다는 것을 Django에게 알려줌
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    
    def __str__(self) :
        return self.choice_text


# 각각의 모델은 Table의 구조를 정의 (=Scheme라고도 하나?)
# 어쨋든 Table의 Data형식을 지정해줌
# 각각의 Columns는 Field라고 불림

class Test(models.Model):

    # 👇🏻 models.CharField는 max_length인자가 필요
    a = models.CharField(max_length=10)

    # 👇🏻 Question.pub_date에 한해서만 인간이 읽기 좋은 형식의 이름을 사용
    b = models.DateTimeField("date published")


class TestDescade(models.Model) :

    c = models.ForeignKey(Test, on_delete=models.CASCADE)
    d = models.CharField(max_length=100)

    # 👇🏻 Integer Field를 생성해줌, 필수 인수는 아님 설정 안해줘도 상관무
    e = models.IntegerField(default=0)
