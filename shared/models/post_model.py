from datetime import datetime
from shared.utils.db_utils import db

class Post(db.Model):
    __tablename__ = 'posts'

    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # counting shares and repost
    share_count=db.Column(db.Integer,default=0,nullable=False)
    repost_count=db.Column(db.Integer,default=0,nullable=False)
