from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://pizza_user:your_password@localhost/pizzadb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False