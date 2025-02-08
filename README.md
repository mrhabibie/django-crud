# Django Simple CRUD

This guide will walk you through the setup and deployment of a Django Simple CRUD web app.

## ⚠️ Minimum Requirements

Ensure your environment meets these requirements:

| Component | Required Version | Installation Link                                 |
| --------- | ---------------- | ------------------------------------------------- |
| Python    | latest           | [Installation](https://www.python.org/downloads/) |

## 📝 Setup Environment

1. Clone Django Simple CRUD project from [this repository](https://github.com/mrhabibie/django-crud.git) :
   - HTTPS
     ```bash
     git clone https://github.com/mrhabibie/django-crud.git
     ```
   - SSH
     ```bash
     git clone git@github.com:mrhabibie/django-crud.git
     ```
2. If you're using Linux / macOS, create Python Virtual Environment :
   ```bash
   python3 -m venv django-crud-venv && source django-crud-venv/bin/activate
   ```
3. Move to project directory :
   ```bash
   cd django-crud
   ```
4. Install all the required project libraries :
   ```bash
   pip install -r requirements.txt
   ```
5. Create migrations :
   ```bash
   python3 manage.py makemigrations
   ```
6. Running migrations :
   ```bash
   python3 manage.py migrate
   ```

## 🚀 Running the Application

1. Make sure [Setup Environment](#-setup-environment) are done.
2. To start the application locally :
   ```bash
   python3 manage.py runserver
   ```
   The application will be available at http://localhost:8000 (the port maybe different or changed if there's any other service already use port 8000, please see at console log).

## Developer Info

Having problem with this project?
[Contact me](https://wa.me/6282143603556).
