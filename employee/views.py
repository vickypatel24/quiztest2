from rest_framework import viewsets, generics, filters, permissions
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Department, Employee, Project, Attendance, Performance
from .serializers import (
    DepartmentSerializer, EmployeeSerializer, ProjectSerializer,
    AttendanceSerializer, PerformanceSerializer
)
from django.db.models import Avg, Count
from django.http import JsonResponse, HttpResponse
import logging

# Configure logging
logger = logging.getLogger(__name__)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'location']
    ordering_fields = ['name', 'budget']


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'position']
    ordering_fields = ['first_name', 'last_name', 'salary', 'hire_date']

    @action(detail=False, methods=['get'])
    def analytics(self, request):
        avg_salary = Employee.objects.all().aggregate(Avg('salary'))
        count_by_dept = Employee.objects.values(
            'department__name').annotate(count=Count('id'))
        return Response({
            'avg_salary': avg_salary,
            'count_by_department': count_by_dept,
        })


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer


class EmployeePerformanceSummary(generics.ListAPIView):
    serializer_class = PerformanceSerializer

    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        return Performance.objects.filter(employee_id=employee_id)


@api_view(['GET'])
def health_check(request):
    logger.info("Health check accessed")
    return JsonResponse({'status': 'ok'})


@api_view(['GET'])
def charts_view(request):
    """
    Serves a simple HTML page with a Chart.js bar chart for employee count by department.
    """
    from .models import Employee
    from django.db.models import Count

    data = Employee.objects.values(
        'department__name').annotate(count=Count('id'))
    labels = [d['department__name'] for d in data]
    counts = [d['count'] for d in data]

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <title>Employee Count by Department</title>
      <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
      <h2>Employee Count by Department</h2>
      <canvas id="myChart" width="400" height="200"></canvas>
      <script>
        const ctx = document.getElementById('myChart').getContext('2d');
        const myChart = new Chart(ctx, {{
            type: 'bar',
            data: {{
                labels: {labels},
                datasets: [{{
                    label: 'Employees',
                    data: {counts},
                    backgroundColor: 'rgba(54, 162, 235, 0.6)',
                }}]
            }},
            options: {{
                scales: {{
                    y: {{
                        beginAtZero: true
                    }}
                }}
            }}
        }});
      </script>
    </body>
    </html>
    """
    logger.info("Charts endpoint accessed")
    return HttpResponse(html)
