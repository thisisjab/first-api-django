from django.urls import path
from django.urls import include
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register('jobs', views.JobViewSet)
router.register('categories', views.CategoryViewSet)
router.register('companies', views.CompnayViewSet)

companies_router = routers.NestedDefaultRouter(router, 'companies', lookup='company')
companies_router.register('reviews', views.ReviewViewSet, basename='company-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(companies_router.urls)),
]
