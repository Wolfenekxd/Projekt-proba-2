from django.shortcuts import render, get_object_or_404,Http404,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from polls.models import polls
from polls.forms import createPoll
from django.views.generic.edit import CreateView,DeleteView
from .db import last_guestions,last_id

# Create your views here.
def avalaible(request):
    latest_question_list = polls.objects.order_by('-Date_of_poll')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/avalaible.html',context)

def detail(request, Poll_id):
  try:
    question = polls.objects.get(pk=Poll_id)
  except ObjectDoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', { 'question': question })    

def results(request, Poll_id):
  question = get_object_or_404(polls, pk=Poll_id)
  return render(request, 'polls/results.html', { 'question': question })  

def vote(request, Poll_id):
    # print(request.POST['choice'])
    question = get_object_or_404(polls, pk=Poll_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, ObjectDoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  


def CreatePoll(request):
  form = createPoll()
  if request.method == 'POST':
    form = createPoll(request.POST)
    if form.is_valid():
      obj = polls()
      obj.id = last_id(polls) + 1
      obj.Poll_question = form.cleaned_data['Poll_question']
      obj.Date_of_poll = form.cleaned_data['Date_of_poll']
      obj.End_of_poll = form.cleaned_data['End_of_poll']
      obj.save()
      return HttpResponseRedirect('/')

  context = {'form':form}

  return render(request, 'polls/polls_form.html', context)


'''

def CreateAnswers(request, Poll_id):
  form = addAnswer()
  if request.method == 'POST':
    form = addAnswer(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')

  context = {'form':form}

  return render(request, 'polls/answers.html',context)      
  '''