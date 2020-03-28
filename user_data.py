import db, bcrypt, hashlib


@db.use
def register_user(cursor, username, text_password):
    """
    Checks for valid username.
    If username is valid, inserts the new user into the database
    """
    query = f""" SELECT username FROM users; """
    cursor.execute(query)
    all_usernames = cursor.fetchall()
    for user in all_usernames:
        if user['username'] == username: 
            return False
    md5_password = hashlib.md5(text_password.encode()).hexdigest()
    query = f""" INSERT INTO users VALUES (DEFAULT, '{username}', '{md5_password}'); """
    cursor.execute(query)
    return True


@db.use
def check_login_credentials(cursor, username, text_password):
    """
    Returns True if the username and password are correct and False if not
    """
    md5_password = hashlib.md5(text_password.encode()).hexdigest()
    query = f""" SELECT * FROM users; """
    cursor.execute(query)
    users = cursor.fetchall()
    for user in users:
        if user['username'] == username and user['password'] == md5_password:
            return True
    return False


