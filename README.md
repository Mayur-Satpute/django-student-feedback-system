📘 Student Feedback System (Django + MySQL CRUD Application)

A clean and beginner-friendly Django web application that allows users to submit, view, update, and delete student feedback.
This project serves as a practical introduction to Django’s MVC pattern, CRUD operations, template handling, and database integration using MySQL (XAMPP).

📌 Features

✔ Submit student feedback (Create)

✔ View all submitted feedback (Read)

✔ Edit/update feedback (Update)

✔ Delete feedback entries (Delete)

✔ Clean and simple user interface

✔ Lightweight CSS styling

✔ Fully functional CRUD cycle

✔ Uses Django ModelForms for validation

✔ MySQL database configuration using XAMPP

🛠️ Tech Stack

Python 3

Django 4

HTML5

CSS (Basic styling, beginner-friendly)

MySQL Database (via XAMPP)

PyMySQL / mysqlclient

📂 Project Structure
crudexam/
│
├── crudapp/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── submit.html
│   │   └── view.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── crudexam/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md

🗄️ MySQL Database Setup (XAMPP)
1. Start XAMPP Services

Start Apache

Start MySQL

2. Create Database

Go to:

http://localhost/phpmyadmin


Create:

feedbackdb

⚙️ Database Configuration in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'feedbackdb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

🔌 Install MySQL Connector
Option 1 — mysqlclient
pip install mysqlclient

Option 2 — PyMySQL
pip install pymysql


Inside crudexam/__init__.py:

import pymysql
pymysql.install_as_MySQLdb()

🚀 Running the Project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Then visit:

http://127.0.0.1:8000/

📝 How It Works
✔ Model

Defines Feedback fields: name, email, message

✔ Form

Uses Django ModelForm for validation

✔ Views

Implements full CRUD functionality

✔ Templates

Home, Submit, View, Update, Base layout

🎨 UI Overview

Simple blue buttons

Clean centered container

Easy-to-read forms

Basic professional table layout

Beginner-friendly HTML & CSS

🌱 Future Enhancements

Add search/filter

Add admin authentication

Add pagination

Add Django messages

Add timestamps

Deploy to cloud (Render/Heroku/PythonAnywhere)

📞 Contact

Name: Mayur
Email: your email here
GitHub: https://github.com/YOUR_USERNAME

LinkedIn: optional

🧾 License

This project is licensed under the MIT License — meaning you are free to use, modify, and distribute this project with proper credit.

📄 MIT License
MIT License

Copyright (c) 
Mayur

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

✅ Conclusion

This project is a solid starting point for developers learning Django and MySQL.
It covers all the essentials of backend development:

Building CRUD applications

Using Django Models, Forms, Views, Templates

Connecting Django to a MySQL database

Designing clean and functional UI

It is beginner-friendly, easy to understand, and makes a great portfolio project to showcase your full-stack learning journey.
