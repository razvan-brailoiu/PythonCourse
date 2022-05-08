from django.urls import path
from Jobs import views

app_name = "jobs"

urlpatterns = [
    path('', views.JobsView.as_view(), name='lista_joburi'),
    path('adaugare/', views.CreateJobsView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateJobsView.as_view(), name='modifica'),
    path('<int:pk>/stergere/', views.delete_Job, name='stergere'),
    path('<int:pk>/activeaza/', views.activate_Job, name='activeaza'),
]