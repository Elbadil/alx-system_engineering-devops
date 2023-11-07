#!/usr/bin/python3
"""Defining a function number_of_subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    req = requests.get(url, allow_redirects=False)

    if req.status_code == 200:
        about_data = req.json()
        number_of_subs = about_data['data']['subscribers']
        return number_of_subs
    else:
        return 0
