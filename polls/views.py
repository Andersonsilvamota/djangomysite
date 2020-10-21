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

    def post(self, request, *args, **kwargs):
        choice = self.get_object().choice_set.get(id=request.POST['choice'])
        choice.votes += 1
        choice.save()
        return super(VoteView, self).get(request, *args, **kwargs)


class SobreView(generic.TemplateView):
    template_name = 'polls/sobre.html'
    def get_queryset(self):
        return redirect('sobre')






'''
def turmaA(request):
    print('')
    return  HttpResponse('Professor: Leonardo')
def turmaB(request):
    print('')
    return  HttpResponse('Professor: Saulo')
'''