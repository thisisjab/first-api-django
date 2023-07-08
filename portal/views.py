from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class JobViewSet(ModelViewSet):
    serializer_class = serializers.JobSerializer

    def get_queryset(self):
        company_id = self.request.query_params.get('company_id')
        if company_id:
            return models.Job.objects.filter(company_id=company_id).prefetch_related('category').all()
        return models.Job.objects.prefetch_related('category').all()



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
