from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from . import filters
from . import models
from . import serializers


class JobViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = filters.JobFilter
    ordering_fields = ['title']
    queryset = models.Job.objects.prefetch_related('category').all()
    search_fields = ['title', 'description']
    serializer_class = serializers.JobSerializer


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.prefetch_related('job_set').all()
    serializer_class = serializers.CategorySerializer


class CompnayViewSet(ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        return models.Review.objects.filter(company_id=self.kwargs['company_pk']).select_related('company').select_related('user').all()

    def get_serializer_context(self):
        return {'company_id': self.kwargs['company_pk']}
