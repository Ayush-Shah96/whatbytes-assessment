# Healthcare Management System Backend

A comprehensive Django-based REST API for a healthcare management system with features like appointment scheduling, medical records, billing, notifications, real-time chat, and more.

## Features

- **Patient Management**: Patient profiles and medical history
- **Doctor Management**: Doctor profiles and availability
- **Appointments**: Schedule, confirm, and manage appointments
- **Prescriptions**: Create and manage prescriptions
- **Medical Records**: Store and retrieve patient medical records
- **Billing System**: Invoice generation and payment tracking
- **Notifications**: Email and in-app notifications
- **Real-time Chat**: WebSocket-based messaging between doctors and patients
- **Reviews**: Doctor ratings and reviews
- **Analytics**: Dashboard with system statistics
- **Audit Logging**: Track all user actions
- **File Management**: Upload and manage files

## Tech Stack

- **Framework**: Django 4.2.7
- **API**: Django REST Framework 3.14.0
- **Database**: PostgreSQL
- **Real-time**: Django Channels with Redis
- **Task Queue**: Celery with Redis
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Containerization**: Docker & Docker Compose

## Project Structure

```
healthcare-proj/
├── healthcare/              # Project settings
│   ├── config/
│   │   ├── settings/
│   │   │   ├── base.py
│   │   │   ├── development.py
│   │   │   └── production.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   └── celery.py
├── core/shared/            # Shared utilities and base classes
├── authentication/          # User authentication
├── patients/               # Patient management
├── doctors/                # Doctor management
├── appointments/           # Appointment scheduling
├── prescriptions/          # Prescription management
├── records/                # Medical records
├── billing/                # Billing and invoicing
├── notifications/          # Notifications system
├── files/                  # File management
├── audit/                  # Audit logging
├── analytics/              # Analytics and reporting
├── reviews/                # Reviews and ratings
├── chat/                   # Real-time messaging
├── templates/emails/       # Email templates
├── requirements/           # Dependency files
└── manage.py              # Django management script
```

## Installation

### Prerequisites
- Python 3.11+
- PostgreSQL 15+
- Redis
- Docker & Docker Compose (optional)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd healthcare-proj
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   source venv/bin/activate      # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements/development.txt
   ```

4. **Create .env file**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/api/`

### Docker Setup

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

2. **Run migrations**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. **Create superuser**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## API Endpoints

- `/api/auth/` - Authentication
- `/api/patients/` - Patient management
- `/api/doctors/` - Doctor management
- `/api/appointments/` - Appointment scheduling
- `/api/prescriptions/` - Prescriptions
- `/api/records/` - Medical records
- `/api/billing/` - Billing and invoices
- `/api/notifications/` - Notifications
- `/api/files/` - File management
- `/api/reviews/` - Reviews and ratings
- `/api/chat/` - Chat and messaging
- `/api/analytics/` - Analytics
- `/api/audit/` - Audit logs

## Admin Panel

Access Django admin at `/admin/` with superuser credentials.

## Testing

Run tests with:
```bash
pytest
```

With coverage:
```bash
pytest --cov=.
```

## Code Quality

Format code with Black:
```bash
black .
```

Check with Flake8:
```bash
flake8
```

Sort imports with isort:
```bash
isort .
```

## Deployment

For production deployment, use the `production.txt` requirements file and set:
```bash
DEBUG=False
DJANGO_SETTINGS_MODULE=healthcare.config.settings.production
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and code quality checks
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support, email support@healthcare.com or open an issue.