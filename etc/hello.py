def hello_app(environ, start_response):
	start_response('200 OK', [('Content-type', 'text/plain')])
    return "\n".join(environ.get('QUERY_STRING').split("&"))
