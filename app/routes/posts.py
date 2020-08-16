from flask import Blueprint, request, jsonify
from app.models import db, Post, User
# from ..auth import require_auth_jobseeker, require_auth_company

bp = Blueprint("posts", __name__, url_prefix='/api/posts')

@bp.route('/<string:email>/')  # fetch all posts of users in the same interests as user.
def fetch_posts_with_follows(email):
    user = User.find_by_email(email)
    subscribers = [i.subscribers for i in user.interests]
    subscribers_ids = [s.id for sub in subscribers for s in sub] # flatten the list
    unique_ids = list(set(subscribers_ids))
    posts = db.session.query(Post, User).join(User).filter(Post.id.in_(unique_ids)).order_by(Post.created_at.desc()).all()
    
    response = {}
    res = [{**p.to_dict(), **{'author': u.as_dict()}} for p, u in posts]
    # for obj in res: 
    #     idx = obj['id']
    #     response[idx] = obj
    # return response # but now posts are not ordered.
    return {'posts': res}

@bp.route('/', methods=["POST"], strict_slashes=False)  # add new post
def add_post():
    data = request.json
    print(f"\n\n\nDATA\n{data}\n\n\n")
    email = data['email']
    userId = User.find_by_email(email).id

    post = Post(body=data['body'], authors_id=userId, created_at='now', updated_at='now')
    db.session.add(post)
    db.session.commit()

    return post.as_dict()

