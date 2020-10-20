from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from polls.models import Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(is_public=True).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    template_name = "polls/detail.html"
    model = Question



class VoteView(generic.DetailView):
    template_name = 'polls/vote.html'
    model = Question

class VoteView(generic.View):

    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        choice = question.choice_set.get(id=request.POST['choice'])
        choice.votes += 1
        choice.save()
        return redirect('detail', question_id)

class SobreView(generic.TemplateView):
    template_name = 'polls/sobre.html'
    def get_queryset(self):
        return redirect('sobre')




class MvotosView(generic.DetailView):
    template_name = 'polls/vote.html'
    model = Question


class voteView(generic.View):

    def post(self, request, question_id):

        question = get_object_or_404(Question, id=question_id)
        choice = question.choice_set.get(id=request.POST['choice'])
        choice.votes += 1
        choice.save()
        return redirect('vote', question_id)


'''
def turmaA(request):
    print('')
    return  HttpResponse('Professor: Leonardo')
def turmaB(request):
    print('')
    return  HttpResponse('Professor: Saulo')
'''