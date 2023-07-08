from django.urls import path
from django.urls import include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('jobs', views.JobViewSet)
router.register('categories', views.CategoryViewSet)
router.register('companies', views.CompnayViewSet)

urlpatterns = [
    path('', include(router.urls))
]
