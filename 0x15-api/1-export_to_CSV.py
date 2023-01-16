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
        lists = []
        lists.append(argv[1])
        lists.append(employeeDetails['username'])
        lists.append(task.get("completed"))
        lists.append(task.get("title"))
        dicts = dict(zip(header, lists))
        data.append(dicts)

    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8') as f:
        writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
        # write multiple rows
        writer.writerows(data)
