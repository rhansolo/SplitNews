import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> hello </h1>'

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/time2')
def get_current_time2():
    return '<p>' + str(time.time()) + '</p>'

if __name__ == '__main__':
    app.debug = True
    app.run()