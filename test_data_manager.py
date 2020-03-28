import db, bcrypt


@db.use
def get_test(cursor):
    query = f"""SELECT * FROM users;"""
    cursor.execute(query)
    return cursor.fetchall()
