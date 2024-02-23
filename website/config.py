import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS")
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD: str | None = os.getenv("MAIL_PASSWORD")
    db_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "../instance/database.db"
    )
    DB_NAME = os.getenv("DB_NAME")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    SESSION_TYPE = os.getenv("SESSION_TYPE")
    SESSION_SQLALCHEMY = os.getenv("SESSION_SQLALCHEMY")
    SESSION_SQLALCHEMY_TABLE = os.getenv("SESSION_TYPE")
    SESSION_SQLALCHEMY_TABLE = os.getenv("SESSION_SQLALCHEMY_TABLE")
    SESSION_SQLALCHEMY_MODEL = os.getenv("SESSION_SQLALCHEMY_MODEL")
