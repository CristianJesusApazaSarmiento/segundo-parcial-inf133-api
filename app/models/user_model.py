from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    roles = db.Column(db.String(50), nullable=False)
    
    def __init__(self, name, email, password, roles):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.roles = roles

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()
    
    def update(self, name=None, email=None, password=None, roles=None):
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if password is not None:
            self.password_hash = generate_password_hash(password)
        if roles is not None:
            self.roles = roles
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)