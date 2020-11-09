from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

class polls(models.Model):
    Poll_question = models.TextField(max_length=256)
    Date_of_poll = models.DateField(null=False)
    End_of_poll = models.DateField(null=False)

    objects = models.Manager ()

class single_answers(models.Model):
    Answer_text = models.TextField(max_length=256)
    result = models.IntegerField()
    Poll_id = models.ForeignKey(polls, on_delete=models.CASCADE)


class voted(models.Model):
    Poll_id = models.ForeignKey(polls, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    voted = models.BooleanField(null=False, default=False)

    class Meta:
        unique_together = (( 'Poll_id','user_id'),)

class createPoll(ModelForm):
    class Meta:
        model = polls
        fields = ['Poll_question','Date_of_poll','End_of_poll']