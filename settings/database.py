from settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

database_driver = settings.DATABASE['default'].get('driver', 'sqlite')
database_dialect = settings.DATABASE['default'].get('dialect', 'sqlite')

user = settings.DATABASE['default'].get('user', 'root')
password = settings.DATABASE['default'].get('password', 'root')
host = settings.DATABASE['default'].get('host', 'localhost')
port = settings.DATABASE['default'].get('port', '3306')
dbname = settings.DATABASE['default'].get('name', 'db_name')

if database_driver in settings.SERVER_DB_DRIVERS:
    database = create_engine(f"{database_driver}+{database_dialect}://{user}:{password}@{host}/{dbname}")
else:
    database = create_engine("sqlite:///sqlite3.db")

Base = declarative_base()
Session = sessionmaker(bind=database)
db_session = Session()
