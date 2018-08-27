from flask_sqlalchemy import SQLAlchemy
from app.views import app

db = SQLAlchemy(app)
class Stock(db.Model):
    pass