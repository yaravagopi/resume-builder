import os

host = os.environ.get('AZURE_DATABASE_HOST', 'localhost')
user = os.environ.get('AZURE_DATABASE_USER', 'root')
password = os.environ.get('AZURE_DATABASE_PASSWORD', 'password')
database = os.environ.get('AZURE_DATABASE_DB', 'database')
ssl_ca = os.environ.get('AZURE_DIGITAL_CERTIFICATE_PEM', 'ssl_ca')


def display():
    print("host: " + host)
    print("user: " + user)
    print("password: " + password)
    print("database: " + database)
    print("ssl_ca: " + ssl_ca)
