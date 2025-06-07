# Django Employee Analytics Project

This project is a Django REST API for managing and analyzing synthetic employee data, including departments, attendance, performance, and projects.

## Features

- Generates synthetic employee data using Faker
- Stores data in SQLite
- REST API endpoints for CRUD and analytics (Django REST Framework)
- Swagger UI for API documentation (drf-yasg)
- Token authentication and rate limiting
- Ready for data visualization integration

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/vickypatel24/quiztest2.git
```

### 2. Create and Activate a Virtual Environment

```sh
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Add the App to Installed Apps

Ensure `'employee'` is in your `INSTALLED_APPS` in `quizedemo/settings.py`.

### 5. Make Migrations

```sh
python manage.py makemigrations employee
python manage.py migrate
```

### 6. Generate Synthetic Data

```sh
python manage.py generate_synthetic_data
```

### 7. Create a Superuser (Optional, for Admin)

```sh
python manage.py createsuperuser
```

### 8. Run the Development Server

```sh
python manage.py runserver
```

### 9. Access the API and Documentation

- Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Admin Panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Notes

- All API endpoints are available under `/api/`.
- Token authentication is enabled. Obtain a token via DRF's token endpoint if needed.
- Rate limiting is set to 1000 requests per user per day.

## Troubleshooting

- If you get `no such table` errors, ensure you have run migrations as shown above.
- If you want to reset the database, delete `db.sqlite3` and the `employee/migrations` files (except `__init__.py`), then repeat the migration steps.

# Django Employee Analytics Project

## API Endpoints

| Endpoint                                   | Method               | Description                                              | Auth Required |
| ------------------------------------------ | -------------------- | -------------------------------------------------------- | ------------- |
| `/api/departments/`                        | GET/POST             | List or create departments                               | Yes           |
| `/api/departments/{id}/`                   | GET/PUT/PATCH/DELETE | Retrieve, update, or delete a department                 | Yes           |
| `/api/employees/`                          | GET/POST             | List or create employees                                 | Yes           |
| `/api/employees/{id}/`                     | GET/PUT/PATCH/DELETE | Retrieve, update, or delete an employee                  | Yes           |
| `/api/employees/analytics/`                | GET                  | Employee analytics (average salary, count by department) | Yes           |
| `/api/projects/`                           | GET/POST             | List or create projects                                  | Yes           |
| `/api/projects/{id}/`                      | GET/PUT/PATCH/DELETE | Retrieve, update, or delete a project                    | Yes           |
| `/api/attendance/`                         | GET/POST             | List or create attendance records                        | Yes           |
| `/api/attendance/{id}/`                    | GET/PUT/PATCH/DELETE | Retrieve, update, or delete an attendance record         | Yes           |
| `/api/performance/`                        | GET/POST             | List or create performance records                       | Yes           |
| `/api/performance/{id}/`                   | GET/PUT/PATCH/DELETE | Retrieve, update, or delete a performance record         | Yes           |
| `/api/employee/{employee_id}/performance/` | GET                  | List performance records for a specific employee         | Yes           |
| `/api/health/`                             | GET                  | Health check endpoint                                    | No            |
| `/api/charts/`                             | GET                  | View employee analytics chart (HTML, Chart.js)           | No            |
| `/swagger/`                                | GET                  | Swagger UI API documentation                             | No            |

**Note:**

- All `/api/` endpoints require authentication (Token).
- Use `/api-token-auth/` (if enabled) to obtain a token.
- Rate limiting is applied to authenticated endpoints.
