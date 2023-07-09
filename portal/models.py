from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
    
    def __str__(self) -> str:
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    category = models.ManyToManyField(Category)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    body = models.CharField(max_length=255, blank=False, null=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
