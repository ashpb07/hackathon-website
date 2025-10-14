## 📁 Project Structure

This project is organized as a monorepo containing distinct Backend (Django) and Frontend (React/JavaScript) applications.

```text
project-dir/
│
├── backend/                                         # Django Backend Application
│   ├── manage.py                                 # Django's command-line utility
│   ├── requirements.txt                         # Python dependency list
│   ├── db.sqlite3                               # Default database file
│   │
│   ├── Django-proj/                             # Main project configuration
│   │   ├── settings.py                         # Project settings
│   │   └── urls.py                             # Root URL configurations
│   │
│   └── api/                                      # Django app for API functionality
│       ├── models.py                           # Database schemas
│       ├── views.py                            # Business logic/API endpoints
│       └── serializers.py                    # Data formatting (Django REST Framework)
│
├── frontend/                                      # React/JavaScript Frontend Application
│   ├── src/                                      # Source code
│   │   ├── components/                        # Reusable UI elements
│   │   ├── pages/                               # Route-specific components
│   │   └── App.jsx                             # Main application component
│   │
│   └── package.json                             # Node.js dependency and script file
│
└── README.md



{
    "elderly": "http://127.0.0.1:8000/elderly/api/elderly/",
    "checkins": "http://127.0.0.1:8000/elderly/api/checkins/",
    "reminders": "http://127.0.0.1:8000/elderly/api/reminders/"
}





POST /medication/api/price-comparison/compare_prices/
{
  "medication_id": "123e4567-e89b-12d3-a456-426614174000",
  "user_lat": 40.7128,
  "user_lng": -74.0060,
  "radius": 5,
  "quantity": 30
}

GET /medication/api/medications/search_medications/?q=metformin

POST /medication/api/price-comparison/find_generic_alternatives/
{
  "medication_id": "123e4567-e89b-12d3-a456-426614174000"
}
