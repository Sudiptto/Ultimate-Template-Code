from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import *
from datetime import datetime, timedelta
from .authUtils import *

auth = Blueprint('auth', __name__)


# sample input
"""
{
    "firstName": "John",
    "lastName": "Doe",
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123"
}
"""
@auth.route('/signup', methods=['POST'])
def signup():
    # Get JSON data from the request body
    data = request.get_json()  

    # Extract data from JSON 
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Validate required fields
    if not (first_name and last_name and username and email and password):
        return jsonify({'error': 'All fields are required'}), 400
    
    # Validate email 
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email type, please try another one'}), 400
    
    # Check for existing user with the same email or username
    if is_email_in_db(email):
        return jsonify({'error': 'Email already in use'}), 409
    
    if is_username_in_db(username):
        return jsonify({'error': 'Username already in use'}), 409

    # Hash password
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create new user
    new_user = User(
        firstName=first_name,
        lastName=last_name,
        username=username,
        email=email,
        password_hash=password_hash,
        date_created=datetime.utcnow()
    )

    # Add user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201


# login user via email and password
{
    "email": "john1@example.com",
    "password": "securepassword123"
}

@auth.route('/login', methods=['POST'])
def login():
    # login via email 
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Validate required fields
    if not (email and password):
        return jsonify({'error': 'All fields are required'}), 400
    
    # Validate email
    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email type, please try another one'}), 400
    
    # Check if user exists via email
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'User does not exist'}), 404
    
    # Check if password is correct
    if not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid password'}), 401
    
    # access JWT (JSON WEB TOKENS) token -> used for authentication
    access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))

    return jsonify(
        {'message': 'Login successful',
         "access_token": access_token
         }), 200
    
