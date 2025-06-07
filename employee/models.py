from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    # ...add more fields as needed...

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    position = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    # ...add more fields as needed...

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    employees = models.ManyToManyField(Employee, related_name='projects')
    status = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    # ...add more fields as needed...

    def __str__(self):
        return self.name


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20)  # Present, Absent, Leave, etc.
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    remarks = models.CharField(max_length=200, blank=True)
    # ...add more fields as needed...

    def __str__(self):
        return f"{self.employee} - {self.date}"


class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    score = models.IntegerField()
    reviewer = models.CharField(max_length=100)
    comments = models.TextField()
    goal_achievement = models.DecimalField(max_digits=5, decimal_places=2)
    promotion_recommended = models.BooleanField(default=False)
    # ...add more fields as needed...

    def __str__(self):
        return f"{self.employee} - {self.review_date}"
