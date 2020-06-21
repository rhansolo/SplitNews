# SplitNews

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the `react-flask-app` directory, you can run:

### `yarn start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `yarn start-api`

Runs the app from the server side using flask.


## About the Project
This project was created for Pinnacle's Everest Hackathon in June 2020. SplitNews allows the user to search for a 
specific topic, (for example, affirmative action), and quickly and easily see a summary of the topic, from both left 
and right leaning sources. We automate the process of looking for sources with varied biases, presenting the user with 
a list of articles from reputable sources from both sides of the aisle, as well as a short and a long summary for
each of the articles. To spread awareness of implicit biases in news sources, each news source is color coded blue 
for left leaning and red for right leaning.

## How it was built
We were able to construct our website using Flask for our backend and React in combination with HTML and CSS to 
construct our frontend. To distinguish biased news sources, we used a combination of website heuristics, and a 
custom trained transformer neural network using Tensorflow and Hugging-Face's Transformer on over 5000 news 
sources, achieving 75% accuracy. We used word and sentence tokenization in NLP to summarize the articles and 
we used the Bing News Search API to obtain links and relevant information to the articles.

## What's Next?
For phase two, we're hoping to make a SplitNews Chrome Extension that automatically helps you any time you're 
reading the news, whether it's something you Googled or a link you received from someone else.
