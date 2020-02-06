#!/usr/bin/python3
"""Return number of subscribers"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Get the total number of subscribers from a subreddit"""
    about = requests.get(
        'https://api.reddit.com/r/{}/about'.format(subreddit),
        headers={'User-Agent': 'FancyRancy'}
    ).json()
    if ('modhash' in about['data']):
        return(0)
    return(about['data']['subscribers'])
