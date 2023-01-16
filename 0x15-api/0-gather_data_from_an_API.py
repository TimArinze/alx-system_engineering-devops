#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
from sys import argv


if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    users_url = main_url + "/users"
    individual = main_url + "/users/{}".format(argv[1])
    user_todos = main_url + "/user/{}/todos".format(argv[1])
    employeeDetails = requests.get(individual).json()
    employeeName = employeeDetails['name']
    usersTotalTasks = requests.get(user_todos).json()
    totalNumberOfTasks = len(usersTotalTasks)
    listOfCompleted = []
    for task in usersTotalTasks:
        if task.get("completed") == True:
            listOfCompleted.append(task)
    numberOfDoneTask = len(listOfCompleted)
    print("Employee {} is done with tasks({}/{}):".
          format(employeeName, numberOfDoneTask, totalNumberOfTasks))
    for task in listOfCompleted:
        print("\t {}".format(task.get("title")))
