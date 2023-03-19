from os import environ

name = name.lower() if (name := environ.get('name')) else 'sqlite'
if driver := environ.get('driver'):
    driver = driver.lower()
database = environ.get('database')
if not database:
    database = 'log_db'

username = environ.get('username')
password = environ.get('password')
host = environ.get('host')
port = environ.get('port')


def create_connection_string():
    # dialect+driver://username:password@host:port/database
    connection_string = f'+{driver}://{username}:{password}@{host}:{port}/{database}'
    if name in ("postgresql",):
        return f"postgresql{connection_string}"

    elif name in ('mysql', ):
        return f'mysql{connection_string}'

    elif name in ('oracle', ):
        return f"oracle{connection_string}"

    elif name in ('microsoft sql server', 'mssql'):
        return f"mssql{connection_string}"

    elif name in ("sqlite", 'sqlite3'):
        # sqlite://<nohostname>/<path>
        return f'sqlite:///{database}.sqlite3'
