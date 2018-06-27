from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published Questions """
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'           

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # Redirect them back #
        return render(request, 'polls/details.html', {
                'question' : question,
                'error_message' : 'You didn\'t select a choice!',
            })
    else:
        selected_choice.votes += 1
        selected_choice.save() 
        # Redirect them #
        return HttpResponseRedirect(reverse('polls:results', args=[question.id,]))
    