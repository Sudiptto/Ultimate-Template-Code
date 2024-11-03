from flask import Blueprint, render_template, request, jsonify
from .models import *
from datetime import datetime

auth = Blueprint('auth', __name__)


# sample input
"""
{
    firstName: "John",
    lastName: "Doe",
    username: "john_doe",
    email: "john@example.com",
    password: "securepassword123"
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

    # Check for existing user with the same email or username
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already in use'}), 409
    if User.query.filter_by(username=username).first():
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
