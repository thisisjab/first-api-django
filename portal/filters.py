from django_filters.rest_framework import FilterSet
from . import models


class JobFilter(FilterSet):

    class Meta:
        model = models.Job
        fields = {
            'company_id': ['exact'],
            'category': ['exact'],
        }