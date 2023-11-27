from datetime import datetime
from extensions import db

class KataKhusus(db.Model):
      __tablename__ = 'kata_khusus'
      id = db.Column(db.Integer, primary_key=True)
      kata = db.Column(db.String(50), nullable=False)
      arti = db.Column(db.String(50), nullable=False)
      format_aksara = db.Column(db.String(50), nullable=False)
      updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
      created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
      deleted_at = db.Column(db.DateTime, nullable=True)

      def __init__(self, kata, arti, format_aksara):
            self.kata = kata
            self.arti = arti
            self.format_aksara = format_aksara
            self.updated_at = datetime.utcnow()
            self.created_at = datetime.utcnow()