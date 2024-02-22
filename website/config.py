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
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    db_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "../instance/database.db"
    )
    DB_NAME = os.getenv("DB_NAME")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    SESSION_TYPE = "sqlalchemy"
    SESSION_SQLALCHEMY = db
    SESSION_SQLALCHEMY_TABLE = "sessions"
    SESSION_SQLALCHEMY_MODEL = "website.models.CustomSessionModel"
