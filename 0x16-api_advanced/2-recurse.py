#!/usr/bin/python3
"""Return list of all hot articles"""
import requests


def recurse(subreddit, hot_list=[])
    """Prints first 10 titles of hot posts"""
    hot_posts = requests.get(
        'https://api.reddit.com/r/{}/hot'.format(subreddit),
        headers={'User-Agent': 'FancyRancy'}
    ).json()
    try:
        i = 0
        while (i < 10):
            post = hot_posts['data']['children'][i]
            print(post['data']['title'])
            i += 1
    except:
        print(None)
