# Flight Booking App ✈️
A full-stack flight booking system using Django (backend), React (frontend), and SQLite (database).

## Technologies Used
- Django + Django REST Framework
- React (Create React App)
- SQLite
- Bootstrap

## Features
- View all available flights
- Search and filter flights by origin, destination, airline
- Book a flight with passenger name and email
- Validate email format and required fields
- View and delete bookings
- Responsive and user-friendly interface with cards layout

## Project Structure
flight-booking-app/
├── flight_backend/      ← Django API + SQLite DB
│   ├── flights/                # Django app with models and views
│   ├── db.sqlite3              # SQLite database file
│   ├── manage.py               # Django project manager
│   └── generate_flights.py     # Script to populate random flights
└── flight-frontend/     ← React UI (Bootstrap styled)
    ├── src/
    │   ├── App.js              # Main component with booking logic
    │   └── components/         # Optional components if split
    ├── public/
    └── package.json

## Setup Instructions

### Backend
cd flight_backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

### Frontend
cd flight-frontend
npm install
npm start

## Usage
- Open browser at: http://localhost:3000
- Backend runs at: http://localhost:8000
- API endpoints:
  • GET /api/flights/
  • POST /api/book/
  • GET /api/bookings/
  • DELETE /api/bookings/<id>/

## Notes
- Make sure both servers are running: Django on port 8000 and React on port 3000.
- Flight data is generated in generate_flights.py
- All data stored locally in flight_backend/db.sqlite3
- Booking includes validation for required fields and email format

## Author
Project created as part of a DevOps course final assignment.
Dima Shmuel 310782164
