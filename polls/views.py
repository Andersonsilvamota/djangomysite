from django.shortcuts import render, get_object_or_404
from polls.models import Question

def index(request, template_name="polls/index.html"):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, template_name, context)

def detail(request, question_id, template_name="polls/detail.html"):
    question = get_object_or_404(Question, id=question_id)
    context = {
        "question": question,
    }
    return render(request, template_name, context)
'''
def sobre(request):
    print('equipe pweb')
    return HttpResponse('minha equipe pweb:anso,mayk,fontineles')

def turmaA(request):
    print('')
    return  HttpResponse('Professor: Leonardo')
def turmaB(request):
    print('')
    return  HttpResponse('Professor: Saulo')
'''