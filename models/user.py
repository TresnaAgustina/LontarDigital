from datetime import datetime
from flask_login import UserMixin
from extensions import db


class User(db.Model, UserMixin):
      __tablename__ = 'users'
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(80), unique=True, nullable=False)
      email = db.Column(db.String(120), unique=True, nullable=False)
      password = db.Column(db.String(120), nullable=False)
      created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
      updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

      def __init__(self, username, email, password):
            self.username = username
            self.email = email
            self.password = password
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()


