from django.urls import path

from . import views

urlpatterns = [
    path('jobs/', views.JobsListView.as_view(), name='jobs_list'),
    path('jobs/<int:id>/', views.JobDetailView.as_view(), name='job_detail'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:id>/', views.CategoryDetailView.as_view(), name='category_detail'),
]