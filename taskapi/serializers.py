from rest_framework.serializers import ModelSerializer
from .models import Tasks, Employer, Group


class TasksSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class EmployerSerializer(ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'