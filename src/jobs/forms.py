from django import forms
from .models import Job, JobApplication


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('created_by',)



class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ('expected_salary_minimum', 'expected_salary_maximum')