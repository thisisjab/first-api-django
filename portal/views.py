from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers


class JobsListView(ListCreateAPIView):
    queryset = models.Job.objects.prefetch_related('category').all()
    serializer_class = serializers.JobSerializer


class JobDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobSerializer


class CategoryListView(ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CompanyListView(ListCreateAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    

class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
