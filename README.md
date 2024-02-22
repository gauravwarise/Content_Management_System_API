# Content Management System
## About
This Django project is a Content Management System (CMS) API that provides the backend functionality for managing and organizing content. The system caters to two types of users: admin and author. Admin users are pre-seeded into the system, while authors can register and log in using their email addresses.Author can create, view, edit and delete contents created by him only.Users can search content by matching terms in title, body, summary and categories

## Prerequisites
Python 

Django 

Djangorestframework

# Install
## Clone the repository fro github
    git clone https://github.com/gauravwarise/Content_Management_System_API.git

## Navigate to the folder
    cd .\Content_Management_System_API\
    
## Install required frameworks and libraries

    pip install -r .\requirements.txt

## Navigate to the project directory

    cd .\CMS_API\

## Perform Migrations

    python manage.py makemigrations
    python manage.py migrate

## create admin using seeding
    python manage.py seed_admin


# Authentication

This project uses JWT token authentication for API requests. To authenticate API requests, include the JWT token in the Authorization header (access_token) of your HTTP requests.


# Endpoints :
The following API endpoints are available:

## User Registration:
### Request

`POST /register`

    {
    "username": "author",
    "email": "author@example.com",
    "full_name": "Author abc",
    "password": "Author@123",
    "phone": "1234563890",
    "address": "123 Main St",
    "city": "Mumbai",
    "state": "Maharashtra",
    "country": "india",
    "pincode": "123456"
    }

### Response
    {
        "status": "success",
        "data": {
            "id": 2,
            "email": "author@example.com",
            "phone": "1234563890",
            "pincode": "123456",
            "last_login": null,
            "is_superuser": false,
            "username": "author@example.com",
            "first_name": "",
            "last_name": "",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2024-02-22T04:15:05.531346Z",
            "full_name": "Author abc",
            "address": "123 Main St",
            "city": "Mumbai",
            "state": "Maharashtra",
            "country": "india",
            "groups": [],
            "user_permissions": []
        },
        "message": "Registration Seccessfully!!!",
        "http_status": 201
    }


## User Login:
### Request

`POST /login`

    {
        "email": "author@example.com",
        "password": "Author@123"
    }

### Response
    {
    "status": "success",
    "data": "",
    "message": "logged in successfully",
    "http_status": 201,
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4NTc
        1NzQ0LCJpYXQiOjE3MDg1NzU0NDQsImp0aSI6IjNjMjE4MjNmMWYyNTQ2YmE
        5MGM0ZDk0OTg3MTk0YWRhIiwidXNlcl9pZCI6Mn0.fhTRm-lD4GZ_ywJ2bCckIuZPUCFghmgXjuZy9sJeGBs"
    }


## Create Content:
### Request

`POST /create`

    {
        "title": "abc",
        "body": "abc",
        "summary":"abc",
        "pdf_file": "path_to_your_pdf_file.pdf",
        "category": "abc"
    }

### Response
    {
        "status": "success",
        "data": {
            "id": 1,
            "title": "abc",
            "body": "abc",
            "summary": "abc",
            "pdf_file": "/pdfs/path_to_your_pdf_file.pdf",
            "category": "abc",
            "author": 2
        },
        "message": "Data Saved",
        "http_status": 201
    }


## Get Content:
### Request

`GET /getcontent`

No Request Body needed

### Response
    {
        "status": "success",
        "data": [
            {
                "id": 1,
                "title": "abc",
                "body": "abc",
                "summary": "abc",
                "pdf_file": "/pdfs/path_to_your_pdf_file.pdf",
                "category": "abc",
                "author": 2
            }
        ],
        "message": "Data Fetch successfully",
        "http_status": 201
    }


## Search Content:
### Request

`GET /getcontent`

query_params:

    /getcontent?search=abc

### Response
    {
        "status": "success",
        "data": [
            {
                "id": 1,
                "title": "abc",
                "body": "abc",
                "summary": "abc",
                "pdf_file": "/pdfs/path_to_your_pdf_file.pdf",
                "category": "abc",
                "author": 2
            }
        ],
        "message": "Data Fetch successfully",
        "http_status": 201
    }


## Update Content:
### Request

`PATCH /update`

    /update/1/

    {
        "title":"abb"
    }

### Response
    {
        "status": "success",
        "data": {
            "id": 1,
            "title": "abb",
            "body": "abc",
            "summary": "abc",
            "pdf_file": "/pdfs/path_to_your_pdf_file.pdf",
            "category": "abc",
            "author": 2
        },
        "message": "Data update successfully",
        "http_status": 201
    }



## Delete Content:
### Request

`DELETE /delete`

    /delete/1/


### Response
    {
        "status": "success",
        "data": "",
        "message": "Data has been deleted",
        "http_status": 201
    }
