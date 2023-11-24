import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST") or "localhost"
db_port = os.getenv("DB_PORT") or 5432
db_db = os.getenv("DB_DB")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_db}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
