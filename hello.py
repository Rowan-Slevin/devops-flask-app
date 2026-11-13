import json
import time
import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host='the-redis-server', port=6379, decode_responses=True)


@app.route('/')
def say_hello():
	data = r.get('hello')
	if data is not None:
		data = json.loads(data)
		# 600 seconds == 10 minutes
		if time.time() - data['time'] <= 600:
			return data['html']

	data = ('<p>Welcome to my Flask App!</p>'
		'<p><a href="/about">About this app</a></p>'
		'<p><a href="/contact">Contact details</a></p>')


	r.set('hello', json.dumps({
		'html': data,
		'time': time.time()
	}))
	return data

@app.route('/about')
def about():
	data = r.get('about')
	if data is not None:
		data = json.loads(data)
		#600 seconds == 10 minutes
		if time.time() - data['time'] <= 600:
			return data['html']


	data = ('<p>This application is running on the Flask web framework.</p>'
		'<p><a href="https://flask.palletsprojects.com/">Visit the Flask website</a></p>'
		'<p><a href="https://python.org/">Visit the Python website</a></p>'
		'<p><a href="/">Back to home</a></p>')

	r.set('about', json.dumps({
		'html': data,
		'time': time.time()
	}))
	return data



@app.route('/contact')
def contact():
	data = r.get('contact')
	if data is not None:
		data = json.loads(data)
		# 600 seconds == 10 minutes
		if time.time() - data['time'] <= 600:
			return data['html']

	data = ('<p>Contact me here: C24386953@mytudublin.ie'
		'<p><a href="/">Back to home</a></p>')
	
	r.set('contact', json.dumps({
		'html': data,
		'time': time.time()
	}))
	return data
