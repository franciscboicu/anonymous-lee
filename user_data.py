import db, bcrypt, hashlib, os
from flask import session

def random_api_key():
    return os.urandom(100)


def is_logged_in():
    if 'logged_in' in session:
        return True
    return False

@db.use
def username_exists(cursor,username):
    query = """
        SELECT *
        FROM users
        WHERE username = %(username)s;
    """
    cursor.execute(query,{'username': username})
    return cursor.fetchone()


@db.use
def register_user(cursor, username, text_password):
    """
    Checks for valid username.
    If username is valid, inserts the new user into the database
    """
    if username_exists(username):
        return False

    query = """INSERT INTO users (username,password) VALUES (%(username)s,%(password)s)"""
    return cursor.execute(query, {"username": username, "password": encrypt_password(text_password)})

@db.use
def check_login_credentials(cursor, username, text_password):
    """
    Returns True if the username and password are correct and False if not
    """
    query = """
        SELECT username
        FROM users
        WHERE username = %(username)s AND password = %(password)s
        ;
    """
    data = {
        "username": username,
        "password": encrypt_password(text_password)
    }
    cursor.execute(query, data)
    return cursor.fetchone()

def encrypt_password(password):
    return hashlib.md5(password.encode()).hexdigest()
