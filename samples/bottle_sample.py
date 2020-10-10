
import bottle
from middleware import SimpleAPIManagementMiddleware
from bottle import route, run, template

def identifier(environ):
    return environ['REMOTE_ADDR']

simple_api_management_options = {
    'KEY': 'add your key here'
}

app = SimpleAPIManagementMiddleware(bottle.app(), simple_api_management_options)

@bottle.route('/test/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

bottle.run(app=app)