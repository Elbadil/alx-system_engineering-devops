#!/usr/bin/python3
"""Python script to export data to in CSV format"""
import csv
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

    # Exporting data in CSV format
    USER_ID = employee_id
    USERNAME = json_user.get('username')
    for tasks in todos_json:
        TASK_COMPLETED_STATUS = tasks['completed']
        TASK_TITLE = tasks['title']
        data_to_add = [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE]
        with open(f'{USER_ID}.csv', mode='a', newline='') as CSVfile:
            writer = csv.writer(CSVfile, delimiter=',', quoting=csv.QUOTE_ALL)
            writer.writerow(data_to_add)
