from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers


class JobsListView(APIView):
    def get(self, request):
        jobs = models.Job.objects.all()
        serializer = serializers.JobSerializer(jobs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.JobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class JobDetailView(APIView):
    def get(self, request, id):
        job = get_object_or_404(models.Job, id=id)
        serializer = serializers.JobSerializer(job)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, id):
        job = get_object_or_404(models.Job, id=id)
        serializer = serializers.JobSerializer(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        job = get_object_or_404(models.Job, id=id)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
