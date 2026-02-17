import os
from flask import Flask
from flask_cors import CORS
from models import db

def create_app():
    app = Flask(__name__)

    # ---------------- CORS ----------------
    frontend_url = os.environ.get('FRONTEND_URL', '*')
    CORS(app, resources={r"/api/*": {"origins": frontend_url}})

    # ---------------- SECRET ----------------
    app.config['SECRET_KEY'] = os.environ.get(
        'SECRET_KEY',
        'dev-key-please-change-in-prod'
    )

    # ---------------- DATABASE ----------------
    database_url = os.environ.get(
        'DATABASE_URL',
        'sqlite:///movielens.db'
    )
