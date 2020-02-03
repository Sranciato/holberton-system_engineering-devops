#!/usr/bin/python3
from json import dump
import requests

if __name__ == "__main__":
    new_list = []
    result = {}
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for user in users:
        for task in tasks:
            if user["id"] == task["userId"]:
                task_dict = {}
                task_dict["task"] = task["title"]
                task_dict["completed"] = task["completed"]
                task_dict["username"] = user["username"]
                new_list.append(task_dict)
        result[user["id"]] = new_list
    with open("todo_all_employees.json", 'w') as file:
        dump(result, file)
