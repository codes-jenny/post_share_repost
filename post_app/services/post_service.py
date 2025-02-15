from shared.models.post_model import Post
from shared.utils.db_utils import db
from shared.models.user_model import User
from shared.models.shared_model import Share

class PostService:
    @staticmethod
    def create_post(user_id, content):
        new_post = Post(user_id=user_id, content=content)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.filter_by(post_id=post_id).first()

    @staticmethod
    def get_posts_by_user(user_id):
        return Post.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_all_posts():
        return Post.query.order_by(Post.created_at.desc()).all()

    @staticmethod
    def update_post(post_id, new_content):
        post = Post.query.filter_by(post_id=post_id).first()
        if post:
            post.content = new_content
            db.session.commit()
        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.query.filter_by(post_id=post_id).first()
        if post:
            db.session.delete(post)
            db.session.commit()
        return post
    
    @staticmethod
    def share_post(user_id,post_id,sent_to_user_id,custom_content=None):
        original_post = Post.query.filter_by(post_id=post_id).first()
        if original_post:
            new_share = Share(user_id=user_id,post_id=post_id,sent_to_user_id=sent_to_user_id,custom_content= custom_content)
            db.session.add(new_share)
            original_post.share_count=original_post.share_count+1
            db.session.commit()
            return new_share
            
        else:
            return None
        
    @staticmethod
    def repost_post(user_id, post_id,custom_content=None):
        original_post = Post.query.filter_by(post_id=post_id).first()
        if original_post:
            repost_content = "Repost from user " + str(original_post.user_id) + ": " + original_post.content
            if custom_content:
                repost_content = f"{custom_content} (Original Post: {original_post.content})"
            new_post = Post(user_id=user_id, content=repost_content)
            db.session.add(new_post)
            original_post.repost_count =original_post.repost_count+ 1
            db.session.commit()
            return new_post
        else:
            return None
          
        
