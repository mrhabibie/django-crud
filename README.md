# Django Simple CRUD

This guide will walk you through the setup and deployment of a Django Simple CRUD web app.

## ⚠️ Minimum Requirements

Ensure your environment meets these requirements:

| Component  | Required Version | Installation Link                                    |
| ---------- | ---------------- | ---------------------------------------------------- |
| Python     | latest           | [Installation](https://www.python.org/downloads/)    |
| PostgreSQL | latest           | [Installation](https://www.postgresql.org/download/) |

## 📝 Setup Environment

1. Clone Django Simple CRUD project from [this repository](https://github.com/mrhabibie/django-crud.git) :
   - HTTPS
     ```sh
     git clone https://github.com/mrhabibie/django-crud.git
     ```
   - SSH
     ```sh
     git clone git@github.com:mrhabibie/django-crud.git
     ```
2. If you're using Linux / macOS, create Python Virtual Environment :
   ```sh
   python3 -m venv django-crud-venv && source django-crud-venv/bin/activate
   ```
3. Move to project directory :
   ```sh
   cd django-crud
   ```
4. Install all the required project libraries :
   ```sh
   pip install -r requirements.txt
   ```

## 💾 Setup Database

1. If you're using Linux / macOS, please update or create service file that located in `~/.pg_service.conf` or if you're using Windows that file is located at `%APPDATA%\postgresql\.pg_service.conf` :

   ```
   [my_service]
   host=localhost
   user=postgres
   dbname=fastprint
   port=5432
   ```

   Please change `host`, `user`, `dbname`, and `port` with yours and make sure you've created the database with name that same with `dbname` above.

## 🚀 Running the Application

1. Make sure [Setup Environment](#-setup-environment) and [Setup Database](#-setup-database) are done.
2. Create migrations :
   ```sh
   python3 manage.py makemigrations
   ```
3. Running migrations :
   ```sh
   python3 manage.py migrate
   ```
4. To start the application locally :
   ```sh
   python3 manage.py runserver
   ```
   The application will be available at http://localhost:8000 (the port maybe different or changed if there's any other service already use port 8000, please see at console log).

## Developer Info

Having problem with this project?
[Contact me](https://wa.me/6282143603556).
