from flask import Flask, render_template, flash, redirect, request, url_for, jsonify, session
import test_data_manager as test_dm
import user_data as ud

app = Flask(__name__)

@app.route("/")
def index():
    return 'index'

#read the message
@app.route("/r/<code>")
def read(code):
    return 'read('+str(code)+')';

#create the message
@app.route("/c")
def create():
    return "create()"

#login
@app.route("/login")
def login():
    return "login()"

#register
@app.router("/register")
def register():
    return "register()"


@app.route('/test')
def test():
    return str(test_dm.get_test())

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
    )
