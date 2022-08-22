import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from api.utils import APIException, generate_sitemap
from api.admin import setup_admin
from api.models import db, User, Posts
import smtplib
from email.message import EmailMessage
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)


app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = "the.wall.application.test@gmail.com"
    msg['from'] = user
    password = "xonfynfdhfueblpf"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(user, password)
        server.send_message(msg)


@app.route('/register', methods=['POST'])
def handle_register():
    body = request.json
    email = request.json.get('email')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    password = request.json.get('password')

    if body is None:
        return "The request body is null", 400
    if not email:
        return 'You need to enter an email', 400
    if not first_name:
        return 'You need to enter an first name', 400
    if not last_name:
        return 'You need to enter an last name', 400
    if not password:
        return 'You need to enter a password', 400

    check_user = User.query.filter_by(email=email).first()

    if check_user:
        return jsonify({
            'msg': 'The email address already exists. Please login to your account to continue.'
        }), 409

    user = User(email=email, first_name=first_name,
                last_name=last_name, password=password)

    db.session.add(user)
    db.session.commit()

    payload = {
        'msg': 'Your account has been registered successfully.',
        'user': user.serialize()
    }
    email_alert("Your Account Information",
                "Your account was successfully created!", email)
    return jsonify(payload), 200


@app.route('/login', methods=['POST'])
def handle_login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({
            "msg": "No account was found. Please check the email used or create an account."
        }), 401

    if password != user.password:
        return jsonify({"msg": "Incorrect password. Please try again."}), 401

    access_token = create_access_token(identity=email)

    payload = {
        'user': user.serialize(),
        "msg": "You've successfully logged in",
        "access_token": access_token
    }

    return jsonify(payload), 200


@app.route('/create_post', methods=['POST'])
@jwt_required()
def handle_new_post():
    body = request.json
    if body is None:
        return jsonify({
            "msg": "body is empty"
        }), 400

    if body["text"] is None:
        return jsonify({
            "msg": "no text found in this post"
        }), 400
    user = User.query.filter_by(email=get_jwt_identity()).first()

    post = Posts(text=body["text"], user=user)

    db.session.add(post)
    db.session.commit()

    payload = {
        'post': post.serialize(),
        "msg": "You've successfully made a post!"
    }

    return jsonify(payload), 200


@app.route('/posts', methods=['GET'])
def handle_get_posts():
    posts = Posts.query.all()
    all_posts = list(map(lambda post: post.serialize(), posts))

    print(all_posts)

    payload = {
        'all_posts': all_posts,
        "msg": "You've successfully retrieved all posts!"
    }

    return jsonify(payload), 200


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)