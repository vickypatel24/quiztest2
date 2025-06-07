from django.core.management.base import BaseCommand
from django.utils import timezone
from employees.models import Department, Employee, Attendance, Performance
from faker import Faker
import random
from decimal import Decimal
from datetime import timedelta, time

fake = Faker()

class Command(BaseCommand):
    help = 'Generate synthetic employee data'

    def handle(self, *args, **kwargs):
        # Create departments
        departments = [
            Department.objects.create(
                name=dept,
                description=fake.text(),
                location=fake.city(),
                budget=Decimal(random.randint(100000, 1000000))
            ) for dept in ['IT', 'HR', 'Finance', 'Marketing']
        ]

        # Create employees
        employees = []
        for _ in range(5):
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                department=random.choice(departments),
                position=fake.job(),
                salary=Decimal(random.randint(30000, 120000)),
                hire_date=fake.date_between(start_date='-5y', end_date='today'),
                phone_number=fake.phone_number(),
                address=fake.address()
            )
            employees.append(employee)

        # Assign department managers
        for dept in departments:
            dept.manager = random.choice(employees)
            dept.save()

        # Generate attendance records (last 30 days)
        for employee in employees:
            for days_ago in range(30):
                date = timezone.now().date() - timedelta(days=days_ago)
                status = random.choices(['PRESENT', 'ABSENT', 'HALF_DAY', 'LEAVE'], 
                                     weights=[0.8, 0.1, 0.05, 0.05])[0]
                
                check_in = time(hour=random.randint(8, 10), minute=random.randint(0, 59))
                check_out = time(hour=random.randint(16, 18), minute=random.randint(0, 59))
                
                Attendance.objects.create(
                    employee=employee,
                    date=date,
                    check_in=check_in,
                    check_out=check_out,
                    status=status,
                    notes=fake.text() if status != 'PRESENT' else '',
                    work_hours=Decimal(random.uniform(6.0, 9.0)),
                    is_remote=random.choice([True, False])
                )

        # Generate performance reviews
        for employee in employees:
            for _ in range(2):  # Two reviews per employee
                Performance.objects.create(
                    employee=employee,
                    review_date=fake.date_between(start_date='-1y', end_date='today'),
                    rating=random.randint(1, 5),
                    productivity_score=Decimal(random.uniform(1.0, 5.0)),
                    communication_score=Decimal(random.uniform(1.0, 5.0)),
                    project_completion=random.randint(60, 100),
                    comments=fake.text(),
                    reviewer=random.choice([e for e in employees if e != employee])
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated synthetic data'))
