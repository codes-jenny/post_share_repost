from datetime import datetime
from shared.utils.db_utils import db

class Share(db.Model):
    __tablename__ = 'shared_posts'

    shared_post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    post_id=db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    custom_content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    sent_to_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)  
    
  
