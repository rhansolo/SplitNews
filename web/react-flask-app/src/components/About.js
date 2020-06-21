import React from "react";

export default () => {
  return (
    <div>
      <h2 className="display-4">About SplitNews</h2>
      <h2>Automate the Search for Truth in the News!</h2>
      <p className='text-left'>SplitNews allows the user to search for a specific topic, (for example, affirmative action), and quickly and easily see a summary of the topic, from both left and right leaning sources. Underneath, the user receives a list of articles from reputable sources from both sides of the aisle, as well as a short summary for each of the articles. To spread awareness of implicit biases in news sources, each news source is color coded blue for left leaning and red for right leaning.</p>
      <p className='text-left'>We were able to construct our website using Flask for our backend and React in combination with HTML and CSS to construct our frontend. To distinguish biased news sources, we used a combination of website heuristics, and a custom trained transformer neural network using Tensorflow and Hugging-Face's Transformer on over 5000 news sources, achieving 75% accuracy. We used word and sentence tokenization in NLP to summarize the articles and we used the Bing News Search API to obtain links and relevant information to the articles.</p>
      <p className='text-left'>Next, we're hoping to make a SplitNews Chrome Extension that automatically helps you when you're reading the news.</p>
    </div>
  );
};