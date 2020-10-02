from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    #path('sobre', views.sobre, name='sobre'),
    #path('turmaa', views.turmaA, name='turmaA'),
    #path('turmab', views.turmaB, name='turmaB'),
]