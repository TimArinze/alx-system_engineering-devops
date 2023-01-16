#!/usr/bin/python3
"""
Gather data from an API
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    individual = main_url + "/users/{}".format(argv[1])
    user_todos = main_url + "/user/{}/todos".format(argv[1])
    employeeDetails = requests.get(individual).json()
    usersTotalTasks = requests.get(user_todos).json()

    data = []
    for task in usersTotalTasks:
        dicts = {}
        dicts.update({"userId": argv[1],
                     "username": employeeDetails.get("username"),
                      "completed": task.get("completed"),
                      "title": task.get("title")})
        data.append(dicts)
    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8') as f:
        header = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL,
                                delimiter=",")
        # write multiple rows
        writer.writerows(data)
