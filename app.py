from flask import Flask, render_template, flash, redirect, request, url_for, jsonify, session
import test_data_manager as test_dm

app = Flask(__name__)

@app.route("/")
def index():
    return 'index'

@app.route("/r/<code>")
def read(code):
    return 'read('+str(code)+')';

@app.route("/c")
def create():
    return "create()"

@app.route('/test')
def test():
    return str(test_dm.get_test())

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
    )
