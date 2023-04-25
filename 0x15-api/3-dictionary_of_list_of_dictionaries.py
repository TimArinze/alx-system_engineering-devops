#!/usr/bin/python3
"""
Gather data from an API 2
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(main_url)).json()
    list_user_ids = []
    for user_ids in users:
        list_user_ids.append(user_ids.get("id"))

    dictionary = {}
    for user_id in list_user_ids:
        todos = requests.get("{}/user/{}/todos".format(main_url,
                             int(user_id))).json()
        user_res = requests.get("{}/users/{}".format(main_url,
                                int(user_id))).json()
        data = []
        username = user_res.get("username")
        for task in todos:
            dicts = {}
            dicts.update({"username": username,
                         "task": task.get("title"),
                          "completed": task.get("completed")})
            data.append(dicts)
        dictionary.update({user_id: data})
    with open('todo_all_employees.json', 'w', encoding='UTF8') as f:
        json.dump(dictionary, f)
