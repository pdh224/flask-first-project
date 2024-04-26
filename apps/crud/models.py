from datetime import datetime
from apps.app import db


class User(db.Model):
    __tablename__="weather"
    id= db.Column(db.Integer, primary_key=True)
    days=db.Column(db.Date, index=True)
    amWeather= db.Column(db.String, index=True)
    pmWeather= db.Column(db.String, index=True)
    temmin= db.Column(db.Integer, index=True)
    temmax= db.Column(db.Integer, index=True)
    created_at=db.Column(db.DateTime, default=datetime.now)
    updated_at= db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )