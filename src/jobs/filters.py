from django_filters import FilterSet, DateFilter

from .models import *


class JobFilter(FilterSet):
    class Meta:
        model = Job
        fields = '__all__'