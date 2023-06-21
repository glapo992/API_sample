"""connection example to restful_api.py module"""
from requests import put, get, post
import json

def add_todo():
    try:
        todo_id=input('id ->')
        todo_data=input('note ->')
        put('http://127.0.0.1:5800/todo-simple/{}'.format(todo_id), data={"note":todo_data}).json()
        return 'item inserted'
    except ConnectionError('connection error'):
        return ConnectionError

def read_todo():
    todo_id=input('id of item to read->')
    return get('http://127.0.0.1:5800/{}'.format(todo_id)).json()

def insert_task():
    headers = {"Content-Type":"application/json"}
    task = input("insert task -> ")
    #task = ("insert task")
    return post('http://127.0.0.1:5800/todos', data=json.dumps({"task":task}), headers=headers).text
def read_all():
    return get('http://127.0.0.1:5800/todos').text



#print(add_todo())

#print(read_todo())


print(insert_task())
print(read_all())