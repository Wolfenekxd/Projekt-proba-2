from django import forms 
from django.forms import ModelForm
from polls.models import polls,single_answers

    
class createPoll(forms.Form):
    Poll_question = forms.CharField(max_length=256)
    Date_of_poll = forms.DateField(required=True)
    End_of_poll = forms.DateField(required=True)