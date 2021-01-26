#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import os

import main


def execution_on_files(path):
    body = ''

    for root, _, files in os.walk(os.path.abspath(path)):
        for file in files:
            m = main.Map(os.path.join(root, file))
            lines = m.print_map().split('\n')
            body += f'<h2>Input for {file} : {m.lines[0] if lines else None}</h2><p>'

            for line in lines:
                body += line[:-1] + '<br />'
            body += '</p><h2>Result</h2><p>'

            if m.validate_map():
                result = m.fill_map()

                for l in result:
                    body += l[:-1] + '<br />'
                body += '</p>'
            else:
                body += f'<h2>Map Error : {file}</h2>'
    return body


name_response = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Biggest Square</title>
</head>
<body style="font-size: 2em; font-family:monospace; text-align:justify;">
    <h1>Biggest Square</h1>
    {body}
</body>
</html>
'''


def not_found(environ, start_response):
    start_response('404 Not Found', [('content-type', 'text/plain')])

    return[b'404 Not Found :(']


def on_get_default(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    print('GET')

    body = execution_on_files('./tests/samples/')

    response = name_response.format(body=body)

    yield response.encode('utf8')


def on_get_generated(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']

    body = ''
    for k, v in params.items():
        if 'map' in k:
            body += f'<h2>Input for {k}</h2><p>'
            lines = main.generate_map_file(*(v.split('-')))

            for line in lines:
                body += line[:-1] + '<br />'
            body += '</p><h2>Result</h2><p>'

            result = main.Map(lines).fill_map()

            for l in result:
                body += l[:-1] + '<br />'
            body += '</p>'

    response = name_response.format(body=body)

    yield response.encode('utf8')


def on_get_input(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    path = './inputs'
    body = execution_on_files(path)

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
        handler = self.pathmap.get((method, path), not_found)

        return handler(environ, start_response)

    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function

        return function


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/', on_get_input)
    dispatcher.register('GET', '/default', on_get_default)
    dispatcher.register('GET', '/gen', on_get_generated)
    httpd = make_server('localhost', 8080, dispatcher)
    httpd.serve_forever()
