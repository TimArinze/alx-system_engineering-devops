#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
from sys import argv
import csv


if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    users_url = main_url + "/users"
    individual = main_url + "/users/{}".format(argv[1])
    user_todos = main_url + "/user/{}/todos".format(argv[1])
    employeeDetails = requests.get(individual).json()
    employeeName = employeeDetails['name']
    usersTotalTasks = requests.get(user_todos).json()
    totalNumberOfTasks = len(usersTotalTasks)
    data = []
    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    for task in usersTotalTasks:
        dicts = {}
        dicts.update({"USER_ID": argv[1],
                     "USERNAME": employeeDetails['username'],
                      "TASK_COMPLETED_STATUS": task.get("completed"),
                      "TASK_TITLE": task.get("title")})
        data.append(dicts)

    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8') as f:
        writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
        # write multiple rows
        writer.writerows(data)
