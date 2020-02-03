#!/usr/bin/python3
from json import dump
import requests
from sys import argv

if __name__ == "__main__":
    task_dict = {}
    new_list = []
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()
    url = "https://jsonplaceholder.typicode.com/todos"
    for task in requests.get(url).json():
        if user["id"] == task["userId"]:
            task_dict["task"] = task["title"]
            task_dict["completed"] = task["completed"]
            task_dict["username"] = user["username"]
            new_list.append(task_dict)
    result = {str(argv[1]): new_list}
    with open(argv[1] + ".json", 'w') as file:
        dump(result, file)
