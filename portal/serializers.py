from rest_framework import serializers

from . import models


class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Job
        fields = ['id', 'title', 'description', 'company', 'category',]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'jobs_count']

    jobs_count = serializers.SerializerMethodField(method_name='retrieve_jobs_count')

    def retrieve_jobs_count(self, category):
        return category.job_set.count()


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Company
        fields = ['id', 'title']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Review
        fields = ['id', 'body', 'company', 'user']
