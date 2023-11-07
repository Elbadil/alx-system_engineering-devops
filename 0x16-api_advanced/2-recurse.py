#!/usr/bin/python3
"""Defining a function recurse"""
import requests


def recurse(subreddit, after_link="", hot_list=[]):
    """Returns a list containing the titles of
    all hot articles for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyAPI'}

    parameters = {
        'after': after_link,
        'limit': 100
    }

    req = requests.get(url, headers=headers,
                       params=parameters,
                       allow_redirects=False)

    if req.status_code == 200:
        hot_data = req.json()
        hot_data_posts = hot_data['data']['children']
        for post in hot_data_posts:
            hot_list.append(post['data']['title'])

        if hot_data['data']['after'] is not None:
            after = hot_data['data']['after']
            return(recurse(subreddit, after, hot_list))
    else:
        return None

    return hot_list
