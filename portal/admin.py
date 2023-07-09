from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'jobs_count']
    list_per_page = 10

    def get_queryset(self, request):
        return models.Category.objects.prefetch_related('job_set').annotate(Count('job')).all()
    
    @admin.display(ordering='name')
    def category_name(self, category):
        url = (reverse('admin:portal_job_changelist')
            + '?'
            + urlencode({
                'category__id': str(category.id)
            }))
        return format_html('<a href="{}">{}</a>', url, category.name)

    @admin.display(ordering='job__count')
    def jobs_count(self, category):
        return category.job__count


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
