import requests
from tqdm import tqdm
import re
import os
from urllib.parse import urljoin
from newspaper import Article
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions
import time
import random
import threading
from collections import deque

BASE_URL = "https://www.allsides.com/"
ALL_TOPICS = "topics-issues"

NEWS_PATH = "news_articles"

BIAS_REGIONS = {
    'left': 'region-triptych-left',
    'center': 'region-triptych-center',
    'right': 'region-triptych-right'
}

def make_snake_case(category):
    return re.sub(r'[\W]+', '', category.replace(" ", "_")).lower()

def scrape_art(article_queue, region, topic):
    while article_queue:
        article = article_queue.popleft()

        try:
            aurl = urljoin(BASE_URL, article.find('div', attrs={'class': 'news-title'}).a['href'])

            st = BeautifulSoup(requests.get(aurl).content, 'html.parser')
            aurl = st.find('div', attrs={'class': 'read-more-story'}).a['href']

            try:
                art = Article(aurl)
                art.download()
                art.parse()
                atext = art.text
            except:
                print("Article failed")

            afile = aurl.split('/')[-1].split('.')[0]
            afiled = os.path.join(NEWS_PATH, topic, region, afile + '.txt')

            while os.path.exists(afiled):
                afile += str(random.randint(0, 9))
                afiled = os.path.join(NEWS_PATH, topic, region, afile + '.txt')

            with open(afiled, 'w') as f:
                f.write(atext)
        except:
            print("art failed")

# s.find_all("div", attrs={"class": "views-row"})

if __name__ == '__main__':
    req = requests.get(urljoin(BASE_URL, ALL_TOPICS))
    soup = BeautifulSoup(req.content, 'html.parser')

    options = ChromeOptions()
    options.add_argument('headless')
    driver = Chrome(options=options)

    topic_dict = {}

    topics = soup.find_all('div', attrs={'class': 'views-row'})
    for topic in topics:
        topic_name = make_snake_case(topic.a.text)
        topic_url = urljoin(BASE_URL, topic.a['href'])

        topic_dict[topic_name] = topic_url

    for topic, url in topic_dict.items():
        if not os.path.exists(os.path.join(NEWS_PATH, topic)):
            for region in BIAS_REGIONS:
                os.makedirs(os.path.join(NEWS_PATH, topic, region))
            print(f"Made folder {topic} with {url}")
        else:
            print(f"Folder {topic} with {url} exists")

        r = requests.get(url)
        s = BeautifulSoup(r.content, 'html.parser')

        pgs = s.findAll('li', attrs={'class': 'pager-current'})
        pgs = [int(pg.text.split()[-1]) for pg in pgs]
        num_pgs = min(*pgs, 10)

        for page in tqdm(range(num_pgs)):
            try:
                driver.get(url + f'&page={page}')
                time.sleep(3)
                while True:
                    if driver.find_elements_by_class_name(BIAS_REGIONS['left']) != []:
                        break
                    time.sleep(1)

                for region in BIAS_REGIONS:
                    a = driver.find_elements_by_class_name(BIAS_REGIONS[region])
                    s = BeautifulSoup(a[0].get_attribute('innerHTML'), 'html.parser')
                    articles = s.find_all('div', attrs={'class': 'allsides-daily-row'})
                    articles = deque(articles)

                    threads = [threading.Thread(target=scrape_art, args=(articles, region, topic)) for i in range(8)]
                    for thread in threads:
                        thread.start()
                    for thread in threads:
                        thread.join()
            except:
                print("page failed")
