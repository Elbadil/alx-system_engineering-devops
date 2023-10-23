#!/usr/bin/python3
"""Python script to export data in Json format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]

    # Retrieve the name of the employee
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    req_user = requests.get(user_url)
    json_user = req_user.json()
    EMPLOYEE_NAME = json_user.get('name')

    # Retrieve the todo items associated with the employee
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos_params = {'userId': employee_id}
    todos_req = requests.get(todos_url, params=todos_params)
    todos_json = todos_req.json()

    # Exporting data in Json format
    USER_ID = employee_id
    USERNAME = json_user.get('username')
    employee_dict = {}
    employee_attr = {}
    list_attr = []
    for tasks in todos_json:
        TASK_COMPLETED_STATUS = tasks['completed']
        TASK_TITLE = tasks['title']
        employee_attr['task'] = TASK_TITLE
        employee_attr['completed'] = TASK_COMPLETED_STATUS
        employee_attr['username'] = USERNAME
        list_attr.append(employee_attr)
        employee_dict[USER_ID] = list_attr

        with open(f'{USER_ID}.json', mode="w", encoding="UTF-8") as JsonFile:
            json.dump(employee_dict, JsonFile)
