from flask import Flask

import backend

app = Flask(__name__)

@app.route('/')
def hello():
    return '<p> Hello </p>'
