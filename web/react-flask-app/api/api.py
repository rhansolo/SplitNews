import time
import json
from flask import Flask, request
import news_analysis.finalsuper as analyzer

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> hello </h1>'

@app.route('/search/query', methods=['POST'])
def get_results():
    data = request.get_json()
    print(data)
    (summary_lst, result_lst) = analyzer.search(data['search'])
    articles = []
    for news in result_lst:
        title = news[0]
        url = news[1]
        pic_json = news[2]
        rating = news[3]
        short = news[4]
        long = news[5]

        single_json = {
            'title' : title,
            'url' : url,
            'pic_json' : pic_json,
            'rating' : rating,
            'short' : short,
            'long' : long
        }    
        articles.append(single_json)
    
    total_json = {
        'leftSummary' : summary_lst[0],
        'middleSummary' : summary_lst[1],
        'rightSummary' : summary_lst[2],
        'articles' : articles
    }

    return total_json

if __name__ == '__main__':
    app.debug = True
    app.run()