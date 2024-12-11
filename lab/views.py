from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import *
import datetime, time

# Create your views here.

def index(request):
    cache_busting_value = str(time.time())
    home_data = Home.objects.first()
    return render(request, 'lab/new.html', {'home_data': home_data, 'cache_busting_value': cache_busting_value})
def syll(request):
    cache_busting_value = str(time.time())
    #syll_data = Syllabus.objects.first()
    return render(request, 'lab/new2.html')#, {'syll_data': syll_data, 'cache_busting_value': cache_busting_value})
def people(request):
    #people_data = People.objects.first()
    return render(request, 'lab/new3.html')
def appointment(request):
    return render(request, 'lab/appointment.html')
def blog(request):
    return render(request, 'lab/blog.html')
def contact(request):
    return render(request, 'lab/new4.html')
def detail(request):
    return render(request, 'lab/detail.html')
def facility(request):
    return render(request, 'lab/new5_facility.html')
def test(request):
    return render(request, 'lab/test.html')

class IndexView(generic.ListView):
    template_name = 'lab/indexlove.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'lab/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'lab/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'lab/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('lab:results', args=(question.id,)))

