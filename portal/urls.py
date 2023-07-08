from django.urls import path

from . import views

urlpatterns = [
    path('jobs/', views.JobsListView.as_view(), name='jobs_list'),
    path('jobs/<int:id>/', views.JobDetailView.as_view(), name='job_detail'),
]