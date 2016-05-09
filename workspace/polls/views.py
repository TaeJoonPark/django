# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from polls.models import Choice, Question
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.forms import *
from django.contrib import messages



def index(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, '문의하기가 성공적으로 전송 되었습니다.')
            
            
        else:
            form = Form()
    return render(request, 'polls/index.html')
# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
    
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
    
# def vote(request, question_id):
#     p = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#             #설문 투표 폼을 다시 보여준다
#             return render(request, 'polls/detail.html', {'question': p, 'error_message': "You didn't select a choice.",})
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         #POST 데이터를 정상적으로 처리하였으면.
#         #항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
#         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})

# Create your views here.
