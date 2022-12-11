from django.urls import path

from . import views

#from django.conf.urls import url

app_name = 'web_apps'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    #url(r'^topics/$', views.topics, name='topics'),  #(not working in old version.)
     # Show all topics.
    path('topics/', views.topics, name='topics'),
     # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]

