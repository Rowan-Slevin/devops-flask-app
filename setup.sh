#1. Update system

sudo apt-get update
$APT dist-upgrade

#2. Packages
$APT install nano vim python-is-python3 python3-venv python3-pip

#3. Virtual Environment
APP_DIR="$HOME/flask_app"
mkdir -p "$APP_DIR"
cd "$APP_DIR"
cd "$APP_DIR"
python -m venv .my_venv
source .my_venv/bin/activate
pip install flask

#4. Writing the app
cat > hello.py <<'PYEOF'
from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return ('<p>Hello, World, I am a Flask app!</p>'
		'<p><a href="/about">About this app</a></p>')

@app.route('/about')
def about():
	return ('<p>This application is runnong on the Flask web framework.</p>'
		'<p><a href="https:flask.palletsprojects.com/"Visit the Flask website</a></p>'
		'<p><a href="/">Back to home</a></p>')

PYEOF

exec flask --app hello run --host=0.0.0.0
