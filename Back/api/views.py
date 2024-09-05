from api.models import Task
from api.serializers import TaskSerializer
from rest_framework import generics

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TasksListDone(generics.ListAPIView):
    queryset = Task.objects.filter(status="DONE")
    serializer_class = TaskSerializer

class TasksListUndone(generics.ListAPIView):
    queryset = Task.objects.filter(status="UNDO")
    serializer_class = TaskSerializer
