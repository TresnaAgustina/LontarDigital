from datetime import datetime
from extensions import db

class Tokenizing(db.Model):
      __tablename__ = 'tokenizing'
      id = db.Column(db.Integer, primary_key=True)
      hasil_tokenize = db.Column(db.Text, nullable=False)
      updated_at = db.Column(db.DateTime, nullable=False)
      created_at = db.Column(db.DateTime, nullable=False)
      deleted_at = db.Column(db.DateTime, nullable=True)

      def __init__(self, hasil_tokenize):
            self.hasil_tokenize = hasil_tokenize
            self.updated_at = datetime.utcnow()
            self.created_at = datetime.utcnow()