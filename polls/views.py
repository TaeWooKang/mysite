from django.http import HttpResponse
from django.shortcuts import render
from .models import Question,Choice
from django.utils import timezone
# Create your views here.

def detail(request, id):
    question = Question.objects.get(id=id)
    return render(request,'polls/detail.html',{'item':question})

def index(request):
    list = Question.objects.all()
    return render(request,'polls/index.html',{'question':list})

def vote(request):
    choice = request.POST['choice']
    c = Choice.objects.get(pk=choice)
    c.votes = c.votes + 1
    c.save()
    return render(request,'polls/vote.html',{'choice':choice})

def data(request,email,number):
    value = request.GET['user_name']
    return HttpResponse(str(number)+"/"+value+"/"+email)

def input_text(request):
    return render(request,'polls/input_text.html',{})

def add_text(request):
    text = request.POST['text']
    # q = Question(question_text = text,
    # pub_date = timezone.now())
    # q.save()
    return HttpResponse('새 질문 "'+text+'"'+' 입력완료')


def result(request,id):
    question = Question.objects.get(pk=id)
    return render(request, 'polls/result.html',{'question':question})