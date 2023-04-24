#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
from sys import argv


if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com/"
    employee_url = main_url + "users/{}".format(argv[1])
    employee_details = requests.get(employee_url).json()
    employee_name = employee_details.get("name")
    todos_url = main_url + "user/{}/todos".format(argv[1])
    todos_details = requests.get(todos_url).json()
    total_num_of_tasks = len(todos_details)
    list_of_completed_tasks = []
    for todo in todos_details:
        if todo.get("completed"):
            list_of_completed_tasks.append(todo)
    total_num_completed = len(list_of_completed_tasks)
    print("Employee {} is done with tasks({:d}/{:d}):".format(employee_name,
          total_num_completed, total_num_of_tasks))
    for completed in list_of_completed_tasks:
        print("\t {}".format(completed.get("title")))
