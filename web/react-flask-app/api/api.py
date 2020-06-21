import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> hello </h1>'

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

if __name__ == '__main__':
    app.debug = True
    app.run()