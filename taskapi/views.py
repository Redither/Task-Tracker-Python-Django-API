from rest_framework.viewsets import ModelViewSet
from .serializers import TasksSerializer, EmployerSerializer, GroupSerializer
from .models import Tasks, Employer, Group
from rest_framework.generics import ListAPIView 
from rest_framework.decorators import action
from rest_framework.response import Response
import django_filters.rest_framework
from django.db.models import Q

class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

class GetTasksView(ListAPIView):
    queryset = Tasks.objects.filter( Q(progress='Не выполнено'))
    serializer_class = TasksSerializer


class EmployerViewSet(ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class GetEmployersView(ListAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'age']

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def delGroup(self,request, pk=None):
        group=self.queryset.get(id=pk)
        group.delete()
        return Response('Группа удалена успешно')

