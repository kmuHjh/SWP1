from cgi import parse_qs
from temcal import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a', [''])[0]
	b = d.get('b', [''])[0]
	if a=='':
		a=0
	else:
		a = int(a)
	if b=='':
		b=0
	else:
		b = int(b)
	response_body = html % {
		'sum' : a+b,
		'mul' : a*b,
	}
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body]
