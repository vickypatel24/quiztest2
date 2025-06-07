from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DepartmentViewSet, EmployeeViewSet, ProjectViewSet,
    AttendanceViewSet, PerformanceViewSet, EmployeePerformanceSummary,
    health_check, charts_view
)

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employee/<int:employee_id>/performance/',
         EmployeePerformanceSummary.as_view(), name='employee-performance-summary'),
    path('health/', health_check, name='health-check'),
    path('charts/', charts_view, name='charts'),
]
