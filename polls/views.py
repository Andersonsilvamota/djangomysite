from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from polls.models import Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.all().order_by("pub_date")[:5]

class DetailView(generic.DetailView):
    template_name = "polls/detail.html"
    model = Question

class VoteView(generic.View):

    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        choice = question.choice_set.get(id=request.POST['choice'])
        choice.votes += 1
        choice.save()
        return redirect('detail', question_id)



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