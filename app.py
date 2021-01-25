#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi


name_response = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Biggest Square</title>
</head>
<body>
    <h1>Biggest Square</h1>
    {body}
</body>
</html>
'''


def not_found(environ, start_response):
    start_response('404 Not Found', [('content-type', 'text/plain')])

    return[b'404 Not Found :(']


def on_get(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    [print(param) for param in params]
    body = ''
    for k, v in params.items():
        body += f'<p>{k} --- {v}</p>'
    response = name_response.format(body=body)

    yield response.encode('utf8')


class PathDispatcher:
    def __init__(self):
        self.pathmap = {}

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO')
        params = cgi.FieldStorage(environ.get('wsgi.input'), environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = {k: params.getvalue(k) for k in params}
        print(method, path, self.pathmap)
        handler = self.pathmap.get((method, path), not_found)

        return handler(environ, start_response)

    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function

        return function


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/', on_get)
    httpd = make_server('localhost', 8080, dispatcher)
    httpd.serve_forever()
