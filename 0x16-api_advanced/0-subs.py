#!/usr/bin/python3
"""
How many sub in Reddit API
"""
import json
import requests


def number_of_subscribers(subreddit):
    headers = {'user-agent': 'MY_AGENT'}
    main_url = "https://api.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(main_url, headers=headers)
    if response.status_code == 200:
        response = response.json()
        return response.get('data').get('subscribers')
    else:
        return 0
