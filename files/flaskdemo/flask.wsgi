'''A Flask application for Apache + mod_wsgi.'''

from flask import Flask
application = Flask(__name__)

@application.route('/')
def index():
    return '<h1>Index Page</h1><a href="hello">Greeter page</a>'

@application.route('/hello')
def hello():
    return 'Hello World' 
