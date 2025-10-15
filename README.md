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

```text
hackathon-website/
├── backend/                                # Main Django Backend Root
│   ├── backend/                            # Project Settings Directory
│   │   ├── settings.py                     # Main configuration (DB, INSTALLED_APPS, CHANNELS)
│   │   ├── urls.py                         # Root URL router (HTTP)
│   │   ├── routing.py                      # Root ROUTING router (WebSocket/ASGI)
│   │   └── wsgi.py / asgi.py               # Server interface files
│   ├── api/                                # Example Django API Application
│   │   ├── models.py                       # Database schemas
│   │   ├── views.py                        # HTTP endpoint logic (DRF Views)
│   │   ├── serializers.py                  # DRF data serialization
│   │   ├── urls.py                         # App-specific HTTP URLs
│   │   └── consumers.py                    # WebSocket handling logic
│   ├── manage.py                           # Django command-line utility
│   └── requirements.txt                    # Python dependencies (Django, DRF, Channels, Redis)
├── frontend/                               # Static Frontend Files
│   ├── index.html                          # Main application structure
│   ├── style.css                           # Styling and presentation
│   └── script.js                           # Client-side logic and API/WebSocket calls
├── assets/                                 # Static assets (images, fonts, etc.)
├── architecture.png                        # System architecture diagram
├── .gitignore
└── README.md


```mermaid
flowchart TD
    %% ===== STYLING =====
    classDef client fill:#4CAF50,stroke:#388E3C,stroke-width:2px,color:white
    classDef server fill:#2196F3,stroke:#1976D2,stroke-width:2px,color:white
    classDef websocket fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:white
    classDef redis fill:#E91E63,stroke:#C2185B,stroke-width:2px,color:white
    classDef channel fill:#9C27B0,stroke:#7B1FA2,stroke-width:2px,color:white
    classDef http fill:#009688,stroke:#00796B,stroke-width:2px,color:white

    %% ===== CLIENT LAYER =====
    subgraph ClientLayer [🌐 Client Layer - Real-time Frontend]
        Browser[<i class='fa fa-chrome'></i><br/>Web Browser<br/>JavaScript WebSocket Client]
        Mobile[<i class='fa fa-mobile'></i><br/>Mobile App<br/>Native WebSocket]
    end

    %% ===== LOAD BALANCER =====
    LB[<i class='fa fa-balance-scale'></i><br/>Load Balancer<br/>NGINX]

    %% ===== ASGI SERVER LAYER =====
    subgraph ServerLayer [⚡ ASGI Server Layer - Connection Handler]
        Daphne1[<i class='fa fa-server'></i><br/>Daphne Server<br/>Instance 1]
        Daphne2[<i class='fa fa-server'></i><br/>Daphne Server<br/>Instance 2]
        Daphne3[<i class='fa fa-server'></i><br/>Daphne Server<br/>Instance 3]
    end

    %% ===== WEB SOCKET LAYER =====
    subgraph WebSocketLayer [🔗 WebSocket Layer - Real-time Protocol]
        Handshake{WebSocket<br/>Handshake}
        WSConnection[<i class='fa fa-plug'></i><br/>Persistent<br/>WebSocket Connection]
        MessageHandler[<i class='fa fa-exchange-alt'></i><br/>Message<br/>Router]
    end

    %% ===== HTTP LAYER =====
    subgraph HTTPLayer [🌍 HTTP Layer - Traditional Requests]
        URLRouter[<i class='fa fa-route'></i><br/>URL Router<br/>urls.py]
        Views[<i class='fa fa-code'></i><br/>View Logic<br/>views.py]
        Auth[<i class='fa fa-shield-alt'></i><br/>Authentication<br/>Middleware]
    end

    %% ===== CHANNELS LAYER =====
    subgraph ChannelsLayer [🔄 Django Channels - Async Handler]
        Consumer1[<i class='fa fa-microchip'></i><br/>WebSocket<br/>Consumer 1]
        Consumer2[<i class='fa fa-microchip'></i><br/>WebSocket<br/>Consumer 2]
        Consumer3[<i class='fa fa-microchip'></i><br/>WebSocket<br/>Consumer 3]
    end

    %% ===== CHANNEL LAYER =====
    subgraph ChannelLayer [📡 Channel Layer - Message Bus]
        Redis[<i class='fa fa-database'></i><br/>Redis Cluster<br/>Message Broker & Cache]
        
        subgraph ChannelGroups [Message Channels]
            ChatChannel[💬 chat.group.<br/>Real-time Chat]
            NotifChannel[🔔 notifications.<br/>User Notifications]
            PresenceChannel[👥 presence.<br/>User Presence]
            GameChannel[🎮 game.session.<br/>Game State]
        end
    end

    %% ===== DATABASE LAYER =====
    subgraph DatabaseLayer [💾 Database Layer - Persistent Storage]
        PostgreSQL[<i class='fa fa-database'></i><br/>PostgreSQL<br/>Primary Database]
        CacheDB[<i class='fa fa-bolt'></i><br/>Redis Cache<br/>Session Storage]
    end

    %% ===== CONNECTIONS =====
    %% Client to Load Balancer
    Browser -- "WebSocket<br/>Initial Connection<br/>wss://" --> LB
    Mobile -- "WebSocket<br/>Initial Connection<br/>wss://" --> LB

    %% Load Balancer to Servers
    LB -- "Distributed<br/>Connections" --> Daphne1
    LB -- "Distributed<br/>Connections" --> Daphne2
    LB -- "Distributed<br/>Connections" --> Daphne3

    %% Server to WebSocket Handshake
    Daphne1 --> Handshake
    Daphne2 --> Handshake
    Daphne3 --> Handshake

    %% Handshake Process
    Handshake -- "1. HTTP Upgrade<br/>Request" --> URLRouter
    URLRouter -- "2. Route to<br/>View/Middleware" --> Auth
    Auth -- "3. Authenticate<br/>User Session" --> Views
    Views -- "4. Return<br/>Handshake Response" --> Handshake
    Handshake -- "5. Upgrade to<br/>WebSocket" --> WSConnection
    WSConnection -- "6. Persistent<br/>Bi-directional" --> MessageHandler

    %% Message Handler to Consumers
    MessageHandler -- "7. Route Messages<br/>to Consumers" --> Consumer1
    MessageHandler -- "7. Route Messages<br/>to Consumers" --> Consumer2
    MessageHandler -- "7. Route Messages<br/>to Consumers" --> Consumer3

    %% Consumers to Channel Layer
    Consumer1 -- "8. Publish/Subscribe<br/>via Channel Layer" --> Redis
    Consumer2 -- "8. Publish/Subscribe<br/>via Channel Layer" --> Redis
    Consumer3 -- "8. Publish/Subscribe<br/>via Channel Layer" --> Redis

    %% Redis to Channels
    Redis -- "9. Message Bus<br/>Broadcast & Groups" --> ChatChannel
    Redis -- "9. Message Bus<br/>Broadcast & Groups" --> NotifChannel
    Redis -- "9. Message Bus<br/>Broadcast & Groups" --> PresenceChannel
    Redis -- "9. Message Bus<br/>Broadcast & Groups" --> GameChannel

    %% Database Connections
    Views -- "SQL Queries<br/>Data Persistence" --> PostgreSQL
    Consumer1 -- "Real-time Data<br/>Operations" --> PostgreSQL
    Consumer2 -- "Real-time Data<br/>Operations" --> PostgreSQL
    Consumer3 -- "Real-time Data<br/>Operations" --> PostgreSQL
    
    Auth -- "Session Data<br/>Fast Access" --> CacheDB
    Redis -- "Cache Warming<br/>Data Sync" --> CacheDB

    %% ===== APPLY STYLES =====
    class Browser,Mobile client
    class LB server
    class Daphne1,Daphne2,Daphne3 server
    class Handshake,WSConnection,MessageHandler websocket
    class URLRouter,Views,Auth http
    class Consumer1,Consumer2,Consumer3 websocket
    class Redis redis
    class ChatChannel,NotifChannel,PresenceChannel,GameChannel channel
    class PostgreSQL,CacheDB server