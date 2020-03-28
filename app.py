from flask import Flask, render_template, flash, redirect, request, url_for, jsonify, session

import test_data_manager as test_dm
import user_data as ud
import message_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("_base.html")

#read the message
@app.route("/r/<code>")
def read(code):
    return 'read('+str(code)+')';

#create the message
@app.route("/c", methods=["GET", "POST"])
def create():
    if request.method == 'POST':
        logged_in = False

        _data = {
            'code': message_data.generate_code(),
            'msg': request.form.get("msg"),
            'password': request.form.get("password"),
        }

        x = message_data.create(_data)

        return(str(x))
    return render_template("create.html")


#login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        text_password = request.form.get('password')
        if ud.check_login_credentials(username, text_password):
            print('Log In successful')
            return redirect('/login')
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
