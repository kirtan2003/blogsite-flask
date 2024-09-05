from datetime import datetime
import secrets
import time
import hashlib
from itsdangerous import URLSafeSerializer as Serializer
from flaskblog import db, LoginManager, app
from flask_login import UserMixin

@LoginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(120),nullable=False, default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    post = db.relationship('Post', backref= 'author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        # Generate a random token
        token = secrets.token_urlsafe(32)

        # Calculate expiration time
        expires_at = int(time.time()) + expires_sec

        # Hash the token for storage (optional but recommended)
        hashed_token = hashlib.sha256(token.encode()).hexdigest()

        # Store the hashed token along with expiration time
        # For example, you might save it in the database
        return token, expires_at

    @staticmethod
    def verify_reset_token(token):
        auth_s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = auth_s.loads(token)['user_id']
        except:
            return None  # token is invalid or expired
        user = User.query.get(user_id)
        return user

    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.image_file}')"


class Post(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

