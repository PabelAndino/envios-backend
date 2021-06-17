from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/'

    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    # serializer = TaskSerializer(data=request.data)
    serializer = TaskSerializer(data=request.data, many=isinstance(request.data, list))
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = 'Cool'
    else:
        data["failure"] = 'Un error Cocurrió'
    return Response(data=data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "Update Successful"
    else:
        data["failure"] = "Ocurriô un Fuck Error"
    return Response(data=data)


@api_view(['DELETE','GET'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    operation = task.delete()
    data = {}
    if operation:
        data['success'] = 'Deleted Succesfuly'
    else:
        data['failure'] = 'Fail to delete'
    return Response(data = data)
