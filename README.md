# Barbershop Appointment Booking API

A RESTful API built with Django REST Framework that allows customers to view barbers and services, check available time slots, and book appointments. Barbers can manage their availability and view upcoming bookings, making scheduling easier and more efficient.

---

## Features

- User registration & login (customers & barbers) using JWT
- CRUD for barbers and services
- Barber availability management
- Appointment booking, rescheduling, and cancellation
- View appointments for logged-in users

---

## Technology

- Django REST Framework
- PostgreSQL (for deployment)
- JWT authentication
- Deployment: Heroku / PythonAnywhere

---

## Models

**User**

- id, username, email, phone, password_hash, role (customer/barber), created_at

**BarberProfile**

- id, user (FK → User), specialty, experience_years

**Service**

- id, name, duration_minutes, price

**Availability**

- id, barber (FK → BarberProfile), date, start_time, end_time

**Appointment**

- id, customer (FK → User), barber (FK → BarberProfile), service (FK → Service), date, start_time, end_time, status (booked/cancelled/completed)

---

## API Endpoints

**Authentication**

- `POST /api/register/` — Register user
- `POST /api/login/` — Login and get JWT token

**Barbers & Services**

- `GET /api/barbers/` — List all barbers
- `GET /api/barbers/{id}/` — Get barber details
- `GET /api/services/` — List services

**Availability**

- `POST /api/barbers/{id}/availability/` — Set availability (barber only)
- `GET /api/availability/?date=YYYY-MM-DD&barber_id={id}` — List open slots

**Appointments**

- `POST /api/appointments/` — Book appointment
- `PUT /api/appointments/{id}/` — Reschedule appointment
- `DELETE /api/appointments/{id}/` — Cancel appointment
- `GET /api/appointments/` — View appointments for logged-in user

---

## Setup

1. Clone the repo:

```bash
git clone https://github.com/Hemnegy/Capstone_Project.git
cd capstone_barbershop
```

## Install dependencies:

pip install -r requirements.txt

## Apply migrations:

python manage.py migrate

## Run the server:

python manage.py runserver
