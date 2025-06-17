from flask import Flask
from flask_migrate import Migrate
from server.config import db  # Absolute import

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')
    
    db.init_app(app)
    Migrate(app, db)
    
    return app

app = create_app()  # Create app instance here