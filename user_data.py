import db, bcrypt, hashlib


@db.use
def check_valid_registration_username(cursor, username):
    """
    Return True if valid, False if not
    """
    query = f""" SELECT username FROM users; """
    cursor.execute(query)
    all_usernames = cursor.fetchall()
    for user in all_usernames:
        if user['username'] == username: 
            return False
    return True


@db.use
def register_user(cursor, username, text_password):
    """
    user_info: list [username, text_password]
    """
    md5_password = hashlib.md5(text_password.encode()).hexdigest()
    query = f""" INSERT INTO users VALUES ({username}, {md5_password}); """
    cursor.execute(query)


@db.use
def check_login_credentials(cursor, username, text_password):
    """
    user_info: list [username, text_password]
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


