from django.conf.urls import url
from django.urls import path
from .import views

app_name = 'polls'
urlpatterns = [
    #127.0.0.1:8000/polls
    url(r'^$', views.index, name= "index"),

    # 127.0.0.1:8000/1
    #url(r'^(?P<question_id>[0-9]+/$)',views.detail, name= "detail"),
    path('<question_id>/', views.detail, name = "detail"),
    # 127.0.0.1:8000/1/results
    url(r'^(?P<question_id>[0-9]+/results$)', views.results, name="results"),

    # 127.0.0.1:8000/1/vote
    url(r'^(?P<question_id>[0-9]+/vote$)', views.vote, name="vote")
]