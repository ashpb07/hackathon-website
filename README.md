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
