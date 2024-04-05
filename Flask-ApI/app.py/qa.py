#importing the flask
from flask import Flask
#setting upt the flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello!'
