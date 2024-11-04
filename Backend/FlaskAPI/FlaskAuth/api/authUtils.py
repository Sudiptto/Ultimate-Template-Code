# File Description: Utility functions for the auth routes.
from .models import *
import re



# function to check if an email is a valid email
def is_valid_email(email):
    # Define a regex pattern for validating an email
    email_regex = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    
    # Check if the email matches the regex pattern
    if not re.match(email_regex, email):
        return False

    return True

# check email is in database
def is_email_in_db(email):
    if User.query.filter_by(email=email).first():
        return True
    return False

# check username is in database
def is_username_in_db(username):
    if User.query.filter_by(username=username).first():
        return True
    return False

# Example usage
"""print(is_valid_email("test@example.com"))  # Should return True
print(is_valid_email("invalid-email"))     # Should return False
print(is_valid_email("sudiptto@gmail.com"))
print(is_valid_email("sudiptto@myhunter.cuny.edu"))
# out look emails
print(is_valid_email("hotmail@outlook.com"))
print(is_valid_email("s@outlook.com"))"""

# more emails
