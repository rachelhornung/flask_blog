'''
Created on Jun 25, 2018

@author: rachel

based on tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
'''
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

