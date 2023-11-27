from datetime import datetime
from extensions import db

class History(db.Model):
        __tablename__ = 'history'
        id = db.Column(db.Integer, primary_key=True)
        #   use text data type for large strings
        teks_asli = db.Column(db.Text(), nullable=False)
        teks_hasil = db.Column(db.Text(), nullable=False)
        updated_at = db.Column(db.DateTime, nullable=False)
        created_at = db.Column(db.DateTime, nullable=False)
        deleted_at = db.Column(db.DateTime, nullable=True)

        def __init__(self, teks_asli, teks_hasil):
                self.teks_asli = teks_asli
                self.teks_hasil = teks_hasil
                self.updated_at = datetime.utcnow()
                self.created_at = datetime.utcnow()