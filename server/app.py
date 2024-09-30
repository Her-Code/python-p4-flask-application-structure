#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

url = '/<string:username>'

url = url.replace('/<', '')

url = url.replace('>', '')

type, parameter = url.split(':')

if __name__ == '__main__':
    app.run(port=5555, debug=True)