from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from simpleapimanagement import SimpleAPIManagementMiddleware

def hello_world(request):
    return Response('Hello World!')

def test(request):
    return Response(request.matchdict["id"])

def identifier(environ, app):
    return environ['REMOTE_ADDR']

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.add_route("test", "/test/{id}")
    config.add_view(hello_world, route_name='hello')
    config.add_view(test, route_name='test')
    config.scan()
    app = config.make_wsgi_app()

    simple_api_management_options = {
        'KEY': 'add your key here',
        'IDENTIFIER': identifier #optional
    }

    app = SimpleAPIManagementMiddleware(app, simple_api_management_options)

    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()