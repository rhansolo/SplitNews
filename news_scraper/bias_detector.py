from newspaper import Article
import threading
from collections import deque
from urllib.parse import urlparse
import os

BIAS_LISTS = 'news_sources'

def scrape_art(article_queue, lqueue, cqueue, rqueue, biases):
    while article_queue:
        article = article_queue.popleft()

        base_site = urlparse(article)[1]

        if base_site not in biases:
            if '.'.join(base_site.split('.')[1:]) in biases:
                base_site = '.'.join(base_site.split('.')[1:])
            else:
                continue

        bias_score = biases[base_site]

        if (bias_score < -0.3 and len(lqueue) < 10):
            to_put = lqueue
        elif (bias_score > 0.3 and len(rqueue) < 10):
            to_put = cqueue
        elif (-0.3 < bias_score and bias_score > 0.5 and len(cqueue) < 10):
            to_put = rqueue
        else:
            continue

        try:
            try:
                art = Article(article)
                art.download()
                art.parse()
                atext = art.text
            except:
                print("Article failed")

            to_put.append({'url': article, 'body': atext, 'bias': bias_score})
        except:
            pass

def get_bias(urllist):
    articles = deque(urllist)
    lqueue = deque()
    cqueue = deque()
    rqueue = deque()

    biases = {}

    with open(os.path.join(BIAS_LISTS, 'left.txt'), 'r') as f:
        urls = f.readlines()
        for url in urls:
            biases[url.strip()] = -1

    with open(os.path.join(BIAS_LISTS, 'left_center.txt'), 'r') as f:
        urls = f.readlines()
        for url in urls:
            biases[url.strip()] = -0.5

    with open(os.path.join(BIAS_LISTS, 'center.txt'), 'r') as f:
        urls = f.readlines()
        for url in urls:
            biases[url.strip()] = 0

    with open(os.path.join(BIAS_LISTS, 'right_center.txt'), 'r') as f:
        urls = f.readlines()
        for url in urls:
            biases[url.strip()] = 0.5

    with open(os.path.join(BIAS_LISTS, 'right.txt'), 'r') as f:
        urls = f.readlines()
        for url in urls:
            biases[url.strip()] = 1

    threads = [threading.Thread(target=scrape_art, args=(articles, lqueue, rqueue, cqueue, biases)) for i in range(8)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return (list(lqueue), list(cqueue), list(rqueue))

if __name__ == '__main__':
    urllist = ['https://www.ft.com/content/fda8c04a-7737-4b17-bc80-d0ed5fa57c6c',
 'https://www.cbsnews.com/news/black-lives-matter-protests-ensue-outside-trumps-keep-america-great-rally-in-tulsa-2020-06-20/',
 'https://www.sfgate.com/news/article/Black-Lives-Matter-painted-at-site-of-former-15354632.php',
 'https://www.chicagotribune.com/suburbs/buffalo-grove/ct-bgc-stevenson-students-black-lives-matter-rally-tl-0625-20200621-dmzr3ri3azbwxptflwphl3vw5q-story.html',
 'https://www.cbsnews.com/news/pence-wouldnt-say-black-lives-matter-interview-juneteenth/',
 'https://www.cnn.com/2020/06/20/us/9-year-old-skater-black-lives-matters-street-washington-dc-trnd/index.html',
 'https://abcnews.go.com/US/man-arrested-threatening-shoot-black-lives-matter-protests/story?id=71359000',
 'https://www.newsweek.com/multiple-people-stabbed-site-uk-black-lives-matter-demonstration-1512362',
 'https://www.usatoday.com/story/sports/nba/2020/06/20/black-lives-matter-bill-russell-child-petition/3228926001/',
 'https://sports.yahoo.com/lou-willia']
    print([len(i) for i in get_bias(urllist)])
