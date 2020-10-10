from flask import Flask
import time
from middleware import SimpleAPIManagementMiddleware

app = Flask(__name__)

def identifier(environ):
    return environ['REMOTE_ADDR']

simple_api_management_options = {
    'KEY': 'add your key here'
}

app.wsgi_app = SimpleAPIManagementMiddleware(app.wsgi_app, simple_api_management_options)

@app.route('/test/<name>')
def hello_world2(name):
    #time.sleep(1.0)
    return 'Hello World!'


@app.route('/')
def hello_world():
    #time.sleep(1.0)
    return 'Hello World!'


#for rule in app.url_map.iter_rules():
#    print(rule)


if __name__ == '__main__':
    app.run()