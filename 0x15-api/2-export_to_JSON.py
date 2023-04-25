#!/usr/bin/python3
"""
Gather data from an API
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    user_res = requests.get("{}/users/{}".format(main_url, argv[1])).json()
    todos = requests.get("{}/user/{}/todos".format(main_url, argv[1])).json()
    user_name = user_res.get("username")
    data = []
    for todo in todos:
        dicts = {}
        dicts.update({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_res.get("username")})
        data.append(dicts)
    dictionary = {}
    dictionary.update({argv[1]: data})

    with open('{}.json'.format(argv[1]), 'w', encoding='UTF8') as f:
        json.dump(dictionary, f)
