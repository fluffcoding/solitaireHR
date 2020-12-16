from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import JobSerializer

from jobs.models import Job


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/jobs-list/',
        'Detail View': '/job-detail/<pk>/',
        'Create': '/job-create/',
        'Update': '/job-update/<pk>/',
        'Delete': '/job-delete/<pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def jobList(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def jobDetail(request, pk):
    jobs = Job.objects.get(id=pk)
    serializer = JobSerializer(jobs, many=False)
    return Response(serializer.data)