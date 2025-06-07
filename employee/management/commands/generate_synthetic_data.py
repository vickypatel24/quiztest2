from django.core.management.base import BaseCommand
from employee.models import Department, Employee, Project, Attendance, Performance
from faker import Faker
import random
from datetime import timedelta, date


class Command(BaseCommand):
    help = 'Generate synthetic employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        # Create Departments
        departments = []
        for _ in range(3):
            dept = Department.objects.create(
                name=fake.company(),
                location=fake.city(),
                head=fake.name(),
                budget=random.randint(100000, 500000)
            )
            departments.append(dept)

        # Create Employees
        employees = []
        for _ in range(5):
            emp = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                department=random.choice(departments),
                hire_date=fake.date_between(
                    start_date='-5y', end_date='today'),
                salary=random.randint(40000, 120000),
                position=fake.job(),
                is_active=True
            )
            employees.append(emp)

        # Create Projects
        projects = []
        for _ in range(2):
            proj = Project.objects.create(
                name=fake.bs().title(),
                description=fake.text(),
                start_date=fake.date_between(
                    start_date='-2y', end_date='today'),
                end_date=fake.date_between(start_date='today', end_date='+1y'),
                status=random.choice(['Active', 'Completed', 'On Hold']),
                budget=random.randint(50000, 200000)
            )
            proj.employees.set(random.sample(
                employees, k=random.randint(1, 3)))
            projects.append(proj)

        # Create Attendance and Performance
        for emp in employees:
            for i in range(10):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_between(
                        start_date='-30d', end_date='today'),
                    status=random.choice(['Present', 'Absent', 'Leave']),
                    check_in=fake.time(),
                    check_out=fake.time(),
                    remarks=fake.sentence()
                )
                Performance.objects.create(
                    employee=emp,
                    review_date=fake.date_between(
                        start_date='-1y', end_date='today'),
                    score=random.randint(1, 10),
                    reviewer=fake.name(),
                    comments=fake.text(),
                    goal_achievement=random.uniform(60, 100),
                    promotion_recommended=random.choice([True, False])
                )
        self.stdout.write(self.style.SUCCESS('Synthetic data generated.'))
