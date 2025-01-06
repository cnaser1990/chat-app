# Django Chat App

A real-time chat application built using Django, Channels, and WebSockets, with SQLite as the database. This app allows users to join chat rooms and send messages in real-time.

## Features

- Real-time communication using WebSockets.
- Join existing chat rooms or create new ones.
- SQLite as the database (for simplicity).
- Basic authentication and user management.

## Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

## Setup

### 1. Clone the repository

```bash
git clone https://your-repository-url.git
cd your-project-folder
```
### 2. Install dependencies

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py migrate
```

### 4. Start the development server

```bash
python manage.py runserver
```

### 5. You can now access the app at:

```bash
http://127.0.0.1:8000
```

