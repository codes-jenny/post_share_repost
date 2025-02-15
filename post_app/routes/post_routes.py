from flask import Blueprint
from post_app.controllers.post_controller import PostController

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/api/posts', methods=['GET'])
def get_all_posts():
    return PostController.get_all_posts()

@post_bp.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    return PostController.get_post(post_id)

@post_bp.route('/api/posts', methods=['POST'])
def create_post():
    return PostController.create_post()

@post_bp.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    return PostController.update_post(post_id)

@post_bp.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    return PostController.delete_post(post_id)

@post_bp.route('/api/users/<int:user_id>/share_posts/<int:sent_to_user_id>', methods=['POST'])
def share_post(user_id, sent_to_user_id):
    return PostController.share_post(user_id, sent_to_user_id)

@post_bp.route('/api/users/<int:user_id>/repost_posts/', methods=['POST'])
def repost_post(user_id):
    return PostController.repost_post(user_id)