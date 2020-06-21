from newspaper import Article
import threading
from collections import deque
from urllib.parse import urlparse
import os
import ktrain
import numpy as np

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


        if (bias_score < -0.3 and len(lqueue) < 100):
            to_put = lqueue
        elif (bias_score > 0.3 and len(rqueue) < 100):
            to_put = cqueue
        elif (-0.3 < bias_score and bias_score < 0.3 and len(cqueue) < 100):
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
    print(len(urllist))
    articles = deque(urllist)
    predictor = ktrain.load_predictor('./news_bias_predictor')

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

    all_urls = list(lqueue) + list(cqueue) + list(rqueue)
    to_analyze = []
    for l in all_urls:
        # to_analyze.extend([l['body'], l['body'][10:], l['body'][20:], l['body'][30:]])
        to_analyze.append(l['body'])

    print("running nn...")

    probs = predictor.predict_proba(to_analyze)
    # probs = np.reshape(probs, (len(all_urls), 4, 3))
    # probs = np.reshape(probs, (len(all_urls), 3))

    print("completed...")

    mn = [0, -1, 1]

    idx = 0

    ll = []
    cl = []
    rl = []

    for l in list(lqueue) + list(cqueue) + list(rqueue):
        ps = probs[idx]
        # ps = sum(ps) / 4
        score = sum(ps * mn)

        if np.argmax(ps) == 1 and score >= -0.3:
            score = -0.35
        if np.argmax(ps) == 0 and score < -0.3:
            score = -0.25
        if np.argmax(ps) == 0 and score > 0.3:
            score = 0.25
        if np.argmax(ps) == 2 and score <= 0.3:
            score = 0.35

        if score < -0.3:
            ll.append(l)
            ll[-1]['bias'] = score
        elif score >= -0.3 and score <= 0.3:
            cl.append(l)
            cl[-1]['bias'] = score
        elif score > 0.3:
            rl.append(l)
            rl[-1]['bias'] = score

        idx += 1

    # for l in list(cqueue):
    #     ps = probs[idx]
    #     ps = sum(ps) / 4
    #     score = sum(ps * mn)
    #     if score < -0.3:
    #         ll.append(l)
    #         ll[-1]['bias'] = score
    #     elif score >= -0.3 and score <= 0.3:
    #         cl.append(l)
    #         cl[-1]['bias'] = score
    #     elif score > 0.3:
    #         rl.append(l)
    #         rl[-1]['bias'] = score

    #     idx += 1

    # for l in list(rqueue):
    #     ps = probs[idx]
    #     ps = sum(ps) / 4
    #     score = sum(ps * mn)
    #     if score < -0.3:
    #         ll.append(l)
    #         ll[-1]['bias'] = score
    #     elif score >= -0.3 and score <= 0.3:
    #         cl.append(l)
    #         cl[-1]['bias'] = score
    #     elif score > 0.3:
    #         rl.append(l)
    #         rl[-1]['bias'] = score

    #     idx += 1

    # for l in list(cqueue):
    #     ps = probs[idx]
    #     ps = sum(ps) / 4
    #     score = sum(ps * mn)
    #     if score >= -0.3 and score <= 0.3:
    #         cl.append(l)
    #         cl[-1]['bias'] = score

    #     idx += 1

    # for l in list(rqueue):
    #     ps = probs[idx]
    #     ps = sum(ps) / 4
    #     score = sum(ps * mn)
    #     if score > 0.3:
    #         rl.append(l)
    #         rl[-1]['bias'] = score

    #     idx += 1

    print([len(i) for i in (lqueue, cqueue, rqueue)])
    print([len(i) for i in (ll, cl, rl)])
    return (ll, cl, rl)

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
