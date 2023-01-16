#!/usr/bin/python3
"""
Gather data from an API
"""
import csv
import requests
from sys import argv


main_url = "https://jsonplaceholder.typicode.com"

Id = int(argv[1])
if __name__ == "__main__":
    user_response = requests.get("{}/users/{}".format(main_url, Id)).json()
    todos = requests.get("{}/user/{}/todos".format(main_url, Id)).json()
    user_name = user_response.get("username")
    data = []
    for task in todos:
        dicts = {}
        dicts.update({"userId": argv[1],
                     "username": user_response.get("username"),
                      "completed": task.get("completed"),
                      "title": task.get("title")})
        data.append(dicts)
    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8') as f:
        for todo in data:
            f.write('"{}", "{}", "{}", "{}"\n'.format(
                Id,
                user_name,
                todo.get('completed'),
                todo.get('title')))
