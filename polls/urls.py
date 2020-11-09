from django.urls import path
from polls import views


urlpatterns = [
    path('avalaible/', views.avalaible, name='polls/avalaible'),
    path('<int:Poll_id>/', views.detail, name='polls/detail'),
    path('<int:Poll_id>/results/', views.results, name='polls/results'),
    path('<int:Poll_id>/vote/', views.vote, name='vote'),
    path('create/',views.CreatePoll, name='polls/polls_form')
]