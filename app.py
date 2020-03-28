from flask import Flask, render_template, flash, redirect, request, url_for, jsonify, session
import test_data_manager as test_dm, message_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("_base.html")

#read the message
@app.route("/r/<code>")
def read(code):
    return 'read('+str(code)+')';

#create the message
@app.route("/c")
def create():
    logged_in = False

    _data = {
        'code': message_data.generate_code(),
        'msg': "message text",
        'password': "1234",
    }

    x = message_data.create(_data)

    return(str(x))

#login
@app.route("/login")
def login():
    return render_template("login.html")

#register
@app.route("/register")
def register():
    return render_template("register.html")


@app.route('/test')
def test():
    return str(test_dm.get_test())

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
    )
