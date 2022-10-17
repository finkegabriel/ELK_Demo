from flask import Flask 
app = Flask(__name__)

@app.route('/api/login')
def login():
    return "not a user"

@app.route('/api/in_log')
def in_log():
    return "taking a log"