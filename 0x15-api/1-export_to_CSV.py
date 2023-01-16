#!/usr/bin/python3
"""
Gather data from an API
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    user_res = requests.get("{}/users/{}".format(main_url, argv[1])).json()
    todos = requests.get("{}/user/{}/todos".format(main_url, argv[1])).json()
    user_name = user_res.get("username")
    data = []
    for task in todos:
        dicts = {}
        dicts.update({"userId": argv[1],
                     "username": user_res.get("username"),
                      "completed": task.get("completed"),
                      "title": task.get("title")})
        data.append(dicts)
    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8') as f:
        header = ['userId', 'username', 'completed', 'title']
        writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
