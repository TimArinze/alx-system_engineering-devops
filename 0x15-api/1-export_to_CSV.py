#!/usr/bin/python3
"""
Gather data from an API
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com/"
    user_url = main_url + "users/{}".format(argv[1])
    user_details = requests.get(user_url).json()
    user_name = user_details.get("username")
    todos_url = main_url + "user/{}/todos".format(argv[1])
    todos_details = requests.get(todos_url).json()
    data = []
    for todo in todos_details:
        dicts = {}
        dicts.update({
                "user_id": argv[1],
                "user_name": user_name,
                "completed": todo.get("completed"),
                "task_title": todo.get("title")})
        data.append(dicts)

    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8') as f:
        header = ['user_id', 'user_name', 'completed', 'task_title']
        writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
