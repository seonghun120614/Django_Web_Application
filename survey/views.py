from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

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
        {view}
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

    global frame, head

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('survey/index.html')

    context = {
        'latest_question_list' : latest_question_list
    }

    view = template.render(context, request)

    return HttpResponse(frame.format(head = head, view = view))


def detail(request, question_id) :

    template = loader.get_template('survey/detail.html')

    try :
        question = Question.objects.get(pk = question_id)
    except :
        raise Http404("Question does not exist")
    
    return HttpResponse(template.render({'question' : question}, request))


def results(request, question_id) :
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id) : 
    return HttpResponse("You're voting on question %s" % question_id)
