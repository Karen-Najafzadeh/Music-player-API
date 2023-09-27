
# Music Player API 📝    
This project is a music player API which i wrote for practicing. A program to list, create and manipulate musics and playlists for different users. it may seem to be super simple but it's just the beginning and will be updated overtime 

## technologies used 🦾🤖

![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## How to launch the project  
To deploy this project clone it on your machine.

First of all you need to create a virtual environment in the directory and install the dipendecies there

This is my favourite way of doing it


```bash
  python -m venv some_name_for_your_venv
```  

Next, activate the environment

on windows:
```bash
  .\your_venv_name\Scripts\activate
``` 
on linux:
```bash
  source\your_venv_name\bin\activate
``` 
Then go ahead and install the essential requirements for this project


```bash
  pip install -r requirements.txt
```  


Finally you need to apply the migrations to create a database
```bash
  python manage.py makemigrations
```  
```bash
  python manage.py migrate
```  

Now you're good to go. just run the project with this command


```bash
  python manage.py runserver
```  


If you prefer to use another database like PostgreSQL or MySQL it's totally fine

# Developement
this project is still under developement and not fully compeleted and will be updated reguallary over time
