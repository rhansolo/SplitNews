import time
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> hello </h1>'

@app.route('/search/query', methods=['POST'])
def get_results():
    data = request.get_json()
    print(data)
    return data

if __name__ == '__main__':
    app.debug = True
    app.run()