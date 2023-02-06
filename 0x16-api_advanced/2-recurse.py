#!/usr/bin/python3
"""
Recurse it
"""
import json
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """recursive function"""
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'MY_AGENT'}
    params = {'after': after, 'count': count, 'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        for value in results.get("children"):
            hot_list.append(value.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    else:
        return None
