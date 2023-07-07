from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self) -> str:
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    category = models.ManyToManyField(Category)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
