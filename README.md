![Simple API Management Logo](https://storage.googleapis.com/simple-api-management-assets/logo.svg) 
# Simple API Management Python WSGI based Frameworks Middleware

## Installation

```bash
$ pip install simple-api-management-wsgi
```

## Usage

Get your API key from our [_Simple API Management_](https://www.simpleapimanagement.com/) UI. your API key will be displayed after signign up and creating an API.

```python
def identifier(environ, app):
    return environ['REMOTE_ADDR']

simple_api_management_options = {
    'KEY': 'add your key here',
    'IDENTIFIER': identifier #optional
}

app.wsgi_app = SimpleAPIManagementMiddleware(app.wsgi_app, simple_api_management_options)
```
