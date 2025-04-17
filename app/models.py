from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class AdCampaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer)
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    interest1 = db.Column(db.Integer)
    interest2 = db.Column(db.Integer)
    interest3 = db.Column(db.Integer)
    impressions = db.Column(db.Integer)
    clicks = db.Column(db.Integer)
    spent = db.Column(db.Float)
    total_conversion = db.Column(db.Integer)
    approved_conversion = db.Column(db.Integer)
    predicted_ctr = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
