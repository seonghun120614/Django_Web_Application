from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Question
from django.shortcuts import render, get_object_or_404

# from django.shortcuts import render
#
# HttpResponse, loader 을 제외해도 됨
#
# def index(request) :
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {'latest_question_list': latest_quesiton_list}
#     return render(request, 'polls/index.html', context)

# from django.shortcuts import get_object_or_404, render
# def detail(request, question_id) :
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'survey/detail.html', {'question': question})

frame = """
<!DOCTYPE html>
<html>
    <head lang="ko">{head}</head>
    <body>
    </body>
</html>
"""

head = f"""
        <meta charset="utf-8">
        <meta name="author" content="Park Seonghun">
        <meta name="description" content="My Schedule && My Diary && My Story. Top Topic is Machine Learning, Deep Learning, Computer programming, Math, Statics, ...">
        <link rel="shortcut icon" href="../static/fabicon.ico">
        <link rel="icon" href="../static/fabicon.ico">
        <title>별로의 놀이터</title>
"""


def index(request) :
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    print("=======================================")
    print(context)
    print("=======================================")
    print(render(request, "survey/index.html"), context)
    print("=======================================")

    return render(request, 'survey/index.html', context)


def detail(request, question_id) :
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'survey/detail.html', {"question" : question})


def results(request, question_id) :
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id) : 
    question = get_object_or_404(Question, pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'survey/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else :
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('survey:results', arg=(question_id, id)))
