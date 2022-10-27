from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TasksViewSet, GetTasksView, EmployerViewSet, GetEmployersView, GroupViewSet

router = DefaultRouter()
router.register('tasks', TasksViewSet )
router.register('employee', EmployerViewSet )
router.register('group', GroupViewSet )


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/tasks/filt', GetTasksView.as_view()),
    path('api/employee/filt', GetEmployersView.as_view()),
]
