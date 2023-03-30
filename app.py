from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html')
