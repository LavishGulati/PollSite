from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    
    # /polls/ 
    path('',views.IndexView.as_view(),name='index'),



    # /polls/5/results/
    path('<int:question_id>/results/', views.ResultView.as_view(), name='results'),

    # /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),


     # /polls/5/
    path('<int:question_id>/', views.DetailView.as_view(), name='details'),







]