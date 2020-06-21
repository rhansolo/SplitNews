import os

NEWS_PATH = "news_articles"

for topic in os.listdir(NEWS_PATH):
    for stance in os.listdir(os.path.join(NEWS_PATH, topic)):
        for file in os.listdir(os.path.join(NEWS_PATH, topic, stance)):
            new_file = file.replace('?', '').replace('&', '').replace('=', '')
            os.rename(os.path.join(NEWS_PATH, topic, stance, file), os.path.join(NEWS_PATH, topic, stance, new_file))
