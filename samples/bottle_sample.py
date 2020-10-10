
import bottle
from simpleapimanagement import SimpleAPIManagementMiddleware
from bottle import route, run, template

def identifier(environ, app):
    return environ['REMOTE_ADDR']

simple_api_management_options = {
    'KEY': 'add your key here',
    'IDENTIFIER': identifier #optional
}

app = SimpleAPIManagementMiddleware(bottle.app(), simple_api_management_options)

@bottle.route('/test/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

bottle.run(app=app)