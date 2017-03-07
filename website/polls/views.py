from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render

def index(request):
    return HttpResponse("Hello world")
def detail(request,question_id):
    return HttpResponse('you are looking at question %s.' % question_id)
def results(request,question_id):
    response = "you are looking at results of quesiton %s."+ models.Question.objects.get(id = question_id).question_text
    return HttpResponse(response % question_id)
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(p.id,)))
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
# Create your views here.
