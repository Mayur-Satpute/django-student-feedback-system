📘 Student Feedback System (Django + MySQL CRUD Application)

This solution empowers institutions with a streamlined mechanism to collect and manage student feedback using Django’s backend architecture and MySQL’s reliability.
The project demonstrates a complete CRUD pipeline and can be extended to enterprise-scale workflows.

⭐ Key Features

CRUD workflow for feedback records

Django ModelForms integration

MySQL (XAMPP) backend

Clean & minimal UI

Scalable and modular structure

Beginner-friendly Django project

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

Open:

http://localhost/phpmyadmin


Create:

feedbackdb

3️⃣ Configure Database in settings.py
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


If it fails:

pip install pymysql


Then add:

import pymysql
pymysql.install_as_MySQLdb()

🚀 How to Launch
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Open:

http://127.0.0.1:8000/

📸 Screenshots

Create a folder in your repo:
/screenshots
Add PNG images inside it with names:

home.png

submit.png

view.png

update.png

🏠 Home Page

📝 Submit Feedback

📄 View Feedback

✏️ Update Feedback

📞 Contact

Developer: Mayur Satpute
Email: mayursatpute246@gmail.com

GitHub: https://github.com/Mayur-Satpute

LinkedIn: https://www.linkedin.com/in/mayur7pute/

🧾 License – MIT
MIT License

Copyright (c)
Mayur Satpute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...

✅ Conclusion

This application showcases a solid beginner-level understanding of Django's MVC workflow, CRUD operations, and database orchestration with MySQL.
Suitable for academic submission, portfolio use, and further upgrades.
