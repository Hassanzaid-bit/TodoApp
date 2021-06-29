from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSeralizer

from .models import Task
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list':'/task-list',
        'Detail View': 'task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk/>'
    }

    return Response(api_urls)
@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSeralizer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSeralizer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer = TaskSeralizer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskupdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSeralizer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("The item has been succesfully deleted")