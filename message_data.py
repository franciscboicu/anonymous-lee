import db, bcrypt, random,string

#
def get_random_string(size=5):
    chars = string.ascii_uppercase
    chars += string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def generate_code():
    #make checks against database to see if unique
    #to be implemented
    return get_random_string()

def create(data):
    message_id = message_insert(data)

    if data['password'] is not None:
        password_insert(message_id, data['password'])

    return message_id

@db.use
def get_message(cursor,code):
    query = """
            SELECT * FROM messages LEFT JOIN messages_passwords
                    ON messages.id = messages_passwords.message_id
                    WHERE messages.code = %(code)s"""
    cursor.execute(query,{'code': code})
    return cursor.fetchone()

@db.use
def message_insert(cursor,data):
    query = """INSERT INTO messages (msg,code) VALUES (%(msg)s,%(code)s) RETURNING id"""
    cursor.execute( query, {
        'msg': data['msg'],
        'code': data['code']
    })
    last_insert_id = cursor.fetchone()
    return last_insert_id['id']

@db.use
def password_insert(cursor, message_id, password):
    query = """INSERT INTO messages_passwords (message_id,password) VALUES (%(message_id)s,%(password)s) """
    cursor.execute(query, {
        'message_id': message_id,
        'password': password
    })


@db.use
def delete_message(cursor, message):
    if message['password'] != None:
        query = f""" DELETE FROM messages_passwords WHERE message_id={message['id']}; """
        cursor.execute(query)
    query = f""" DELETE FROM messages WHERE id={message['id']}; """
    cursor.execute(query)  