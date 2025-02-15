from flask import request
from post_app.services.post_service import PostService
from post_app.views.post_view import PostView
from shared.models.post_model import Post

class PostController:
    @staticmethod
    def get_all_posts():
        posts = PostService.get_all_posts()
        
        return PostView.render_posts(posts), 200

    @staticmethod
    def get_post(post_id):
        post = PostService.get_post_by_id(post_id)
        if not post:
            return PostView.render_error('Post not found'), 404
        return PostView.render_post(post), 200

    @staticmethod
    def create_post():
        data = request.get_json()
        user_id = data.get('user_id')
        content = data.get('content')

        post = PostService.create_post(user_id, content)
        return PostView.render_success('Post created successfully',{ "post_id":post.post_id}), 201

    @staticmethod
    def update_post(post_id):
        data = request.get_json()
        new_content = data.get('content')

        post = PostService.update_post(post_id, new_content)
        if post:
            return PostView.render_success('Post updated successfully', {"post_id":post.post_id}), 200
        return PostView.render_error('Post not found'), 404

    @staticmethod
    def delete_post(post_id):
        post = PostService.delete_post(post_id)
        if post:
            return PostView.render_success('Post deleted successfully', {"post_id":post.post_id}), 200
        return PostView.render_error('Post not found'), 404

    @staticmethod
    def share_post(user_id,sent_to_user_id):
        data = request.get_json()
        post_id = data.get('post_id')
        custom_content = data.get('custom_content') 
        
        if not post_id:
            return PostView.render_error('Post ID is required'), 400
        
        
        if not sent_to_user_id:
            return PostView.render_error('Reciever id  is required'), 400

        shared_post = PostService.share_post(user_id, post_id,sent_to_user_id, custom_content)
        if shared_post:
            original_post = Post.query.filter_by(post_id=post_id).first()
            return PostView.render_success(
                'Post Shared successfully',
                PostView.render_shared_post(shared_post, original_post)
            ), 200


        return PostView.render_error('Post not found'), 404

    @staticmethod
    def repost_post(user_id):
        data = request.get_json()
        post_id = data.get('post_id')
        custom_content = data.get('custom_content') 
        if not post_id:
            return PostView.render_error('Post ID is required'), 400
        
        
        reposted_post = PostService.repost_post(user_id, post_id,custom_content)
        if reposted_post:
            original_post = Post.query.filter_by(post_id=post_id).first()
            return PostView.render_success(
                'Post Reposted successfully',
                PostView.render_reposted_post(reposted_post, original_post)
            ), 200

            

        return PostView.render_error('Post not found'), 404
