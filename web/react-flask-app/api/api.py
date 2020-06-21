import time
import json
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
    return json.dumps({'time': time.time()})

@app.route('/search/<query>', methods=['GET'])
def get_results(query):
    return { 'query' : query}

if __name__ == '__main__':
    app.debug = True
    app.run()