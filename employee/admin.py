from django.contrib import admin
from .models import Department, Employee, Project, Attendance, Performance

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Attendance)
admin.site.register(Performance)
