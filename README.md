# Employee Data Analytics API

A Django-based web application that generates synthetic employee data, provides REST API endpoints for analytics, and visualizes data through Swagger UI.

## Features

- Synthetic employee data generation
- SQLite database storage
- REST API endpoints for data analytics
- Interactive data visualization using Swagger UI

## Setup Instructions

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Start development server:

```bash
python manage.py runserver
```

5. Access the API documentation at:
   http://localhost:8000/swagger/

## API Endpoints

- `/api/employees/` - List all employees
- `/api/analytics/` - Get analytical summaries

## Technology Stack

- Django
- Django REST Framework
- drf-yasg (Swagger/OpenAPI)
- SQLite
