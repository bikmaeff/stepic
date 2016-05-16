def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    params = environ['QUERY_STRING'].split('&')
    body = [item + "\r\n" for item in params]   
    return body
