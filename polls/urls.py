from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/vote/', views.VoteView.as_view(), name='detail'),
    path('sobre', views.SobreView.as_view(), name='sobre'),
    #path('turmaa', views.turmaA, name='turmaA'),
    #path('turmab', views.turmaB, name='turmaB'),


]