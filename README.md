📘 Student Feedback System (Django + MySQL CRUD Application)

This solution empowers institutions with a streamlined mechanism to collect and manage student feedback using Django’s robust backend architecture and MySQL’s proven reliability.
The project demonstrates an end-to-end CRUD pipeline and can be extended to enterprise-scale workflows.

⭐ Key Features

CRUD workflow for feedback records

Django ModelForms integration

MySQL (XAMPP) database backend

Streamlined UX with clean, minimal UI

Modular and scalable project structure

Production-ready architecture fundamentals

🛠️ Tech Stack
Layer	Technology
Backend	Django 4 (Python 3)
Database	MySQL (XAMPP)
Frontend	HTML5, CSS
ORM Layer	Django ORM
Connector	mysqlclient / PyMySQL
📂 Project Architecture
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

🗄️ MySQL Configuration (XAMPP)
1️⃣ Start Services

Apache ✔

MySQL ✔

2️⃣ Create Database

Go to:

http://localhost/phpmyadmin


Create a new database named:

feedbackdb

3️⃣ Configure Django (settings.py)
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

4️⃣ Install MySQL Connector

Preferred:

pip install mysqlclient


If mysqlclient fails:

pip install pymysql


Then add inside crudexam/__init__.py:

import pymysql
pymysql.install_as_MySQLdb()

🚀 How to Launch

Run migrations:

python manage.py makemigrations
python manage.py migrate


Start server:

python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

📞 Contact

Developer: Mayur Satpute
Email: mayursatpute246@gmail.com

GitHub: https://github.com/Mayur-Satpute

LinkedIn: https://www.linkedin.com/in/mayur7pute/

🧾 License — MIT
MIT License

Copyright (c)
Mayur Satpute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
(license text remains same)

✅ Conclusion

This application reflects a strong baseline understanding of Django's MVC workflow, CRUD operations, and database orchestration with MySQL.
The architecture is scalable, maintainable, and well-structured — ideal for academic evaluation, portfolio presentation, or future enterprise upgrades.
