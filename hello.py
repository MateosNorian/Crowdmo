from flask import Flask
app = Flask(__name__)

from markupsafe import escape
from flask import render_template

@app.route('/')
def index():
    return 'Index page!'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'Hello {username}'

@app.route('/post/<int:post_id>')
def show_fake_post(post_id):
    return f'{post_id} is the post id'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name):
    return render_template('index.html', name=name)