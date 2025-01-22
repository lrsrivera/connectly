from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer

# CREATE (POST)
@api_view(['POST'])
def create_user(request):
    """Create a new user"""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_task(request):
    """Create a new task"""
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_user(request):
    print(request.data)  # Debug line
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



# READ (GET)
@api_view(['GET'])
def get_users(request):
    """Retrieve all users"""
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_tasks(request):
    """Retrieve all tasks"""
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# UPDATE (PUT)
@api_view(['PUT'])
def update_task(request, task_id):
    """Update a task by its ID"""
    try:
        task = Task.objects.get(id=task_id)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)


# DELETE (DELETE)
@api_view(['DELETE'])
def delete_task(request, task_id):
    """Delete a task by its ID"""
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return Response({'message': 'Task deleted successfully'}, status=200)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)
