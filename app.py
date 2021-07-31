from flask import Flask
from flask.templating import render_template
from pyfladesk import init_gui
#from routes import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    init_gui(app, window_title="Medicine Management")