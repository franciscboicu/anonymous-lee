import db, bcrypt

#user data
@db.use
def get_test(cursor):
    query = f"""SELECT * FROM users;"""
    cursor.execute(query)
    return cursor.fetchall()
