import os
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
