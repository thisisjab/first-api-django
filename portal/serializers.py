from rest_framework import serializers

from . import models


class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Job
        fields = ['id', 'title', 'description', 'company', 'category',]