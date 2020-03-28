from flask import Flask, render_template, flash, redirect, request, url_for, jsonify, session

import test_data_manager as test_dm
import user_data as ud
import message_data

app = Flask(__name__)
app.secret_key = ud.random_api_key()

@app.route("/")
def index():
    username = session['username'] if ud.is_logged_in() else None
    return render_template("_base.html", username=username)

#read the message
@app.route("/r/<code>")
def read(code):
    if not ud.is_logged_in(): return redirect('/login')
    return 'read('+str(code)+')';

#create the message
@app.route("/c")
def create():
    if not ud.is_logged_in(): return redirect('/login')

    _data = {
        'code': message_data.generate_code(),
        'msg': "message text",
        'password': "1234",
    }

    x = message_data.create(_data)

    return(str(x))

#login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if ud.is_logged_in():
        return redirect('/')
    if request.method == 'POST':
        username = request.form.get('username')
        text_password = request.form.get('password')
        if ud.check_login_credentials(username, text_password):
            session['username'] = username
            session['logged_in'] = True
            return redirect('/')
        else:
            print('Invalid username or password')
            return redirect('/login')
    return render_template("login.html")

#register
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        text_password = request.form.get('password')
        if not ud.register_user(username, text_password):
            print('Username already in use')
            return redirect('/register')
        else:
            print('Registration complete')
        
    return render_template("register.html")


@app.route('/test')
def test():
    return str(test_dm.get_test())

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
    )
