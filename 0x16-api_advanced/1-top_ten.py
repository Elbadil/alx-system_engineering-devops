#!/usr/bin/python3
"""Defining a function top_ten"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts
    listed for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    headers = {'User-Agent': 'MyAPI'}

    try:
        req = requests.get(url, headers=headers, allow_redirects=False)

        if req.status_code == 200:
            hot_data = req.json()
            hot_data_posts = hot_data['data']['children']
            count = 10
            for post in hot_data_posts:
                print(post['data']['title'])
                count -= 1
                if count == 0:
                    break
        else:
            print('None')
    except Exception:
        print('None')
