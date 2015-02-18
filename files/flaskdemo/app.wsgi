'''
Based on the example application from https://www.python.org/dev/peps/pep-0333/

The function name is "application" as it's the default setting for mod_wsgi's
WSGICallableObject directive.
'''

def application(environ, start_response):
    """Greet the universe, then show the environment"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    environment_sorted_string = '\n'.join(
        ["%s: %s" % (key,environ.get(key)) for key in sorted(environ.keys())]
    )
    return ['Hello world!\n%s'% environment_sorted_string] 
