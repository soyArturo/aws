import json
import os
from django.http import HttpResponse, JsonResponse
from pymongo import MongoClient


def get_db_handle():
    """Method to create a connection to a database
    Returns:
        db_handle: Database handle
    """
    host = os.environ.get('MONGO_INITDB_HOST')
    port = os.environ.get('MONGO_INITDB_PORT')
    username = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
    password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
    db_name = os.environ.get('MONGO_INITDB_NAME')
    try:
        client = MongoClient(host=host,
                             port=int(port),
                             username=username,
                             password=password
                             )
        db_handle = client[db_name]
        return db_handle
    except Exception:
        return None


def index(request):
    """Method to render the index page
    Returns:
        render: Rendered index page
    """
    db_handle = get_db_handle()
    if db_handle is not None:
        employees = db_handle.employee
        employee = {
            'name': 'John',
            'age': '30',
            'salary': '20000'
        }
        employees.insert_one(employee).inserted_id

        return HttpResponse("Connected to database")
    else:
        return HttpResponse("Could not connect to database")


def get_employees(request):
    """Method to get all employees
    Returns:
        render: Rendered index page
    """
    db_handle = get_db_handle()
    if db_handle is not None:
        employees = db_handle.employee
        employees_list = employees.find()
        return JsonResponse(json.dump(employees_list))
    else:
        return HttpResponse("Could not connect to database")
