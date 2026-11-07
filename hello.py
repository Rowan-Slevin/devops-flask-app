from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return ('<p>This is another string!</p>'
	'<p><a href="/about">About this app</a></p>')

@app.route('/about')
def about():
	return ('<p>This application is running on the Flask web framework.</p>'
		'<p><a href="https:..flask.palletsprojects.com/">Visit the Flask website</a></p>'
		'<p><a href="/">Back to home</a></p>')

@app.route('/contact')
def contact():
	return ('<p>Contact me here: C24386953@mytudublin.ie'
		'<p><a href="/">Back to home</a></p>')
