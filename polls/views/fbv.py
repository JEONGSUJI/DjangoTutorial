from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from ..models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    # Template: /polls/templates/polls/results.html
    # question_id에 해당하는 Question을 보여주고
    # 해당 Question에 연결된 Choice목록을 보여주며
    # 보여줄 때, votes값도 같이 보여줘야함

    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question' : question,
    }

    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    # 특정 Question에 해당하는 특정 Choice의 votes를 1늘리기
    # 이후 특정 Question에 해당하는 results페이지로 이동

    # question = Question.objects.filter(pk=question_id)

        # 아무것도 선택되지 않은 경우 detail page로 다시 이동

        # GET parameter로 전달된 question_id에 해당하는 Quesion객체
        question = get_object_or_404(Question,pk=question_id)

        # form의 POST요청으로 전달된 Choice의 pk값
        try :
            choice_pk = request.POST['choice']
        except:
            return redirect('polls:detail', question_id=question_id)

        # 전달받은 Choice pk에 해당하는 Choice 객체
        choice = get_object_or_404(Choice, pk=choice_pk)

        # 선택된 Choice의 votes값을 1 증가
        choice.votes += 1
        choice.save()

        return redirect('polls:results', question_id=question_id)

    # return HttpResponse(f"You're voting on question {question_id}.")