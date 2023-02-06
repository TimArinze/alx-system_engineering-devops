#!/usr/bin/python3
"""
Top ten
"""
import json
import requests


def top_ten(subreddit):
    """first ten titles"""
    url = "https://api.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'user-agent': 'MY_USER'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response = response.json()
        for post in response["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
