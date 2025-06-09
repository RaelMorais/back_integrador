### ✨ Final Project Backend 
The final project of backend, where an api was developed in django rest for smart city,
where it controls sensors and environments. 

### ⚒ How do start? 
Guide on how to run the project locally on your machine. 

### 📋 Prerequisites
To start the project you need:

[![Python](https://skillicons.dev/icons?i=py)]("https://www.python.org/downloads/")
[![Postman](https://skillicons.dev/icons?i=postman)]("https://www.postman.com/downloads/")
[![MySql](https://skillicons.dev/icons?i=mysql)]("https://dev.mysql.com/downloads/windows/installer/8.0.html")

### 📦 Getting Started 
To start the project download it with

```git clone https://github.com/RaelMorais/back_integrador.git```

After clone, start venv and activate venv 

```python -m venv .env``` --> Create venv 

```.\.env\Scripts\activate``` --> Activate venv 

And install requirements using 

```pip install -r requirements.txt```

Then navigate to the folder where manage.py is located using

```cd smart_city```

### ⚙️ Environment Configuration

In ```setting.py``` change a Workbench user and password

```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'here_your_database_name',
          'USER': 'your_user_in_workbench',
          'PASSWORD': 'your_password_in_workbench',
          'HOST': 'localhost',  # --->Mysql Ip---<
          'PORT': '3306',       # porta padrão
      }
  }
```

>> 🧠 Don't forget to create the database in MySQL Workbench before running the server.

### ▶️ Run Project 

To run project use: 

```python manage.py runserver```

👤 Create a superuser to access the admin panel:

```python manage.py createsuperuser```

### 📚 Documentation & GraphQL Access
Swagger Docs: http://127.0.0.1:8000/api/swagger/

  >>🔐 Use your credentials in Authorize button.
      
GraphQL Playground: http://127.0.0.1:8000/api/graphql/

  Full Postman Documentation: 📄 Click ![here]("https://documenter.getpostman.com/view/41755227/2sB2x3oYq8") to view
  


### Built With
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=FFFFFF)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=GraphQL&logoColor=FFFFFF)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=FFFFFF)
![Swagger](https://img.shields.io/badge/Swagger-222222?style=for-the-badge&logo=Swagger&logoColor=85EA2D)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=FFFFFF)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=FFFFFF)
