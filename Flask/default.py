from app import app
from flask import render_template

@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/aboutus')
def index():
    return(render_template('aboutus.html'))