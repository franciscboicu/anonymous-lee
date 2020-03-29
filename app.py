from flask import Flask, render_template, flash, redirect, request, url_for, jsonify, session

import test_data_manager as test_dm
import user_data as ud
import message_data

app = Flask(__name__)
app.secret_key = ud.random_api_key()

@app.route("/")
def index():
    return render_template("create.html")

#read the message
@app.route("/r/<code>")
def read(code):
    if not ud.is_logged_in(): return redirect('/login')
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
        user_registered = ud.register_user(request.form.get('username'), request.form.get('password'))
        if user_registered == False:
            return redirect(url_for("register"))
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('logged_in')
    return redirect(url_for('index'))

@app.route('/test')
def test():
    return str(test_dm.get_test())

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
    )
