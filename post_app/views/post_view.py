class PostView:
    @staticmethod
    def render_post(post):
        return {
            "post_id": post.post_id,
            "user_id": post.user_id,
            "content": post.content,
            "created_at": post.created_at,
            "updated_at": post.updated_at
        }

    @staticmethod
    def render_posts(posts):
        return [PostView.render_post(post) for post in posts]

    @staticmethod
    def render_error(message):
        return {"error": message}
    
    @staticmethod
    def render_success(message, data=None):
        response = {"message": message}
        if data :
            response["data"] = data
        return response
    
    @staticmethod
    def render_shared_post(shared_post, original_post):
        return{
            "shared_post_id": shared_post.shared_post_id,
            "original_post_id": original_post.post_id,
            "shared_by_user_id": shared_post.user_id,
            "sent_to_user_id": shared_post.sent_to_user_id,
            "shared_at": shared_post.created_at,
            "original_content":original_post.content,
            "custom_content": shared_post.custom_content,
            "share_count": original_post.share_count,
            "repost_count": original_post.repost_count,
        }

    @staticmethod
    def render_reposted_post(reposted_post, original_post):
        return {
            "reposted_post_id": reposted_post.post_id,
            "original_post_id": original_post.post_id,
            "shared_by_user_id": reposted_post.user_id,
            "Reposted_at": reposted_post.created_at,
            "reposted_content": reposted_post.content,
            "share_count": original_post.share_count,
            "repost_count": original_post.repost_count,
        }
        
