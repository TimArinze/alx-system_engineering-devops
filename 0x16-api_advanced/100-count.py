#!/usr/bin/python3
"""
Count it recursively move through the pagination
"""
import requests
import json


def count_words(subreddit, word_list, after="", count=0):
    """recursive function that queries the Reddit API,
    parses the title of all hot articles, 
    and prints a sorted count of given keywords"""
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'MY_AGENT'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        after = results.get("after")
        new_list = []
        for word in word_list:
            new_list.append(word.lower())
        for value in results.get("children"):
            if value.get("data") in new_list:
                count += 1
        if after is not None:
            return count_words(subreddit, word_list, after, count)
        return count
    else:
        return None
