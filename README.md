# MineAdmin Dashboard

A modern web dashboard to monitor and manage Minecraft servers remotely.

## Features
- Live server status monitoring
- Player management
- Remote console
- Discord webhook notifications
- Server performance graphs
- REST API
- SQLite database

## Tech Stack
- Backend: Python, Flask, SQLite
- Frontend: HTML, CSS, JavaScript
- Libraries: mcstatus, psutil, discord-webhook, APScheduler

## Installation
```bash
git clone https://github.com/AmarOP99/MineAdmin.git
cd MineAdmin
pip install -r requirements.txt
python app.py

## 📸 Screenshots

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Players
![Players](screenshots/playerlist.png)

### Login
![Login](screenshots/login.png)

### Settings
![Settings](screenshots/settings.png)

MineAdmin/
├── app.py
├── config.py
├── requirements.txt
├── routes/
│   ├── dashboard.py
│   ├── players.py
│   ├── auth.py
│   └── settings.py
├── services/
│   ├── minecraft.py
│   ├── monitoring.py
├── templates/
│   ├── dashboard.html
│   ├── players.html
│   ├── login.html
│   └── settings.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── database/
│   ├── models.py
│   └── db.py
└── screenshots/

 Future Improvements

    User authentication system

    Dark mode

    Server settings manager

    Backup button