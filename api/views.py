from http import server
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from api.serializers import TaskSerializer
from .models import Task


@api_view(['GET'])
def links(request):

    urls = {
        'api/': 'all links',
        'api/task-list' : 'task list view',
        'api/task-detail/<int:pk>/' : 'task detail view',
        'api/task-create' : 'task create view',
        'api/task-update/<int:pk>/' : 'task update view',
        'api/task-delete/<int:pk>/' : 'task delete view',
    }

    return Response(urls)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    task = get_object_or_404(Task, id=pk)
    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def task_update(request, pk):
    
    task = get_object_or_404(Task, id=pk)
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)

    if request.method == 'PUT':
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()

    return Response(serializer.data)


@api_view(['GET','DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'GET':
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        task.delete()

    return Response()




