from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('turmaa', views.turmaA, name='turmaA'),
    path('turmab', views.turmaB, name='turmaB'),
]