import platform

# Session constants
COMPUTER_NAME = platform.node()

# Hashing constants
SALT_LENGTH = 32

# Controllers prefix for app, need to be with the dot at the end
APP_CONTROLLERS_PATH = "app.controllers."

SERVER_DB_DRIVERS = [
    'mysql',
    'postgresql',
    'mssql',
    'oracle'
]

DATABASE = {
    'default': {
        'driver': 'mysql',
        'dialect': 'pymysql',
        'name': 'pyqt5',
        'user': 'root',
        'password': 'Local_root_123',
    },
    'mysql': {
        'driver': 'mysql',
        'dialect': 'pymysql',
        'name': 'db_name',
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': '3306',
    },
    'postgresql': {
        'driver': 'postgresql',
        'dialect': 'psycopg2',
        'name': 'db_name',
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': '3306',
    },
    'oracle': {
        'driver': 'oracle',
        'dialect': 'cx_oracle',
        'name': 'db_name',
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': '3306',
    },
    'mssql': {
        'driver': 'mssql',
        'dialect': 'pyodbc',
        'name': 'db_name',
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': '3306',
    },
}
