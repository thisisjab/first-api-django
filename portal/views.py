from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class JobViewSet(ModelViewSet):
    queryset = models.Job.objects.prefetch_related('category').all()
    serializer_class = serializers.JobSerializer


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.prefetch_related('job_set').all()
    serializer_class = serializers.CategorySerializer


class CompnayViewSet(ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class ReviewViewSet(ModelViewSet):
    queryset = models.Review.objects.select_related('company').select_related('user').all()
    serializer_class = serializers.ReviewSerializer
