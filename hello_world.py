import bottle

@bottle.route('/')
def home_page():
	return  "<html><title>Learning Bottle</title><body>Hello World</body></html>"

@bottle.route('/testpage')
def test_page():
	return "<html><body>This is a test Page !\n</body></html>"

bottle.debug(True)
bottle.run(host='localhost', port = 8080)

