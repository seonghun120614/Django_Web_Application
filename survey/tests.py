import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase) :

    def test_was_published_recently_with_future_question(self) :
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = time)

        self.assertIs(future_question.was_published_recently(), False) # 원하는 값 2번째 인자 실제 인자 1번째 인자
        