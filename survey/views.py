from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import Question, Choice


def index(request) :
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'survey/index.html', context)


def detail(request, question_id) :
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'survey/detail.html', {"question" : question})


def results(request, question_id) :
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "survey/results.html", {'question' : question})


'''
class IndexView(generic.ListView) :
    template_name = 'survey/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self) :
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView) :
    model = Question
    template_name = 'survey/detail.html'

class ResultsView(generic.DetailView) :
    model = Question
    template_name = 'survey/results.html'
'''



def vote(request, question_id) : 

    if request.method = "GET" :
        pass
    
    elif request.method = "POST" :
        question = get_object_or_404(Question, pk=question_id)

        try :
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'survey/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else :
            selected_choice.vote += 1
            selected_choice.save()

            # post 데이터를 성공적으로 처리한 후는 항상 HttpResponseRedirect를 반환해야함.
            # reverse는 '/polls/3/results/'를 반환
            return HttpResponseRedirect(reverse('survey:results', args=(question_id,)))
