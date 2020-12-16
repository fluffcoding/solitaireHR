from django.contrib import admin
from . models import Job, Industry, FunctionalArea, JobApplication


admin.site.register(Job)
admin.site.register(Industry)
admin.site.register(FunctionalArea)
admin.site.register(JobApplication)