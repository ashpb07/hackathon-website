# 🧠 Hackathon Website

A fullstack web application built using **Django**, **Django REST Framework**, and **PostgreSQL**, designed for hackathon-style rapid prototyping and scalable development.  
It combines a RESTful backend API with a dynamic HTML/CSS/JS frontend.

---

## 📖 Table of Contents

- [About](#about)
- [Architecture Overview](#architecture-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contact](#contact)

---

## 🧾 About

This project serves as a **hackathon boilerplate** demonstrating a modular fullstack architecture:

- **Django** handles the backend logic, ORM, and authentication.
- **Django REST Framework (DRF)** provides API endpoints for data exchange.
- **Frontend (HTML/CSS/JS)** interacts with the API to deliver an interactive user interface.

---

## 🏗️ Architecture Overview

Below is the high-level architecture of this project:

![Architecture Diagram](./assets/arc.png)

**Flow Summary:**

1. **Client (Browser)** — HTML, CSS, and JavaScript handle structure, styling, and interactivity.
2. **Web Server** — Django processes requests, renders templates, and communicates with DRF internally.
3. **API Layer** — Django REST Framework exposes endpoints returning JSON responses.
4. **Database** — PostgreSQL stores and retrieves persistent data.
5. **Data Flow** — Client ⇄ Django ⇄ DRF ⇄ PostgreSQL.

---

## 🧩 Tech Stack

| Layer | Technology | Description |
|-------|-------------|-------------|
| **Frontend (Client)** | **HTML5**, **CSS3**, **JavaScript (Vanilla JS)** | Handles UI structure, styling, and interactivity. Communicates with backend via HTTP/HTTPS requests. |
| **Backend (Web Server)** | **Django (Python Web Framework)** | Manages server-side logic, routing, and serves templates or APIs. |
| **API Layer** | **Django REST Framework (DRF)** | Exposes RESTful API endpoints for frontend communication. Serializes data between Django models and JSON. |
| **Database** | **PostgreSQL** | Stores and retrieves persistent application data. |
| **Communication** | **HTTP / HTTPS**, **JSON** | Enables client–server communication. |
| **Runtime / Language** | **Python 3.x**, **JavaScript (ES6)** | Primary languages for backend and frontend. |


---

## ✨ Features

- **Elderly Health Monitoring** — Daily check-ins and vital tracking dashboard.  
- **AI Health Assistant** — 24/7 intelligent chatbot support for medical queries.  
-  **Secure Patient Portal** — Simple login system with personal health records.  
-  **Real-Time Updates** — Patient status and alerts for caregivers.  
-  **Modular Design** — Django + DRF + PostgreSQL for scalability.  
-  **Analytics Ready** — Extendable for data visualization and predictive insights.  

---

## 🗂️ Project Structure

hackathon-website/
│
├── backend/ # Django backend
│ ├── manage.py
│ ├── db.sqlite3 / PostgreSQL
│ ├── requirements.txt
│ ├── backend/ # project settings
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ └── api/ # example Django app
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ └── urls.py
│
├── frontend/ # HTML, CSS, JS frontend
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── assets/
│ └── architecture.png # architecture diagram
│
├── .gitignore
└── README.md


