"""connection example to restful_api.py module"""

from requests import put, get

def add_todo():
    try:
        todo_id=input('id ->')
        todo_data=input('note ->')
        put('http://127.0.0.1:5800/{}'.format(todo_id), data={"note":todo_data}).json()
        return 'item inserted'
    except ConnectionError('connection error'):
        return ConnectionError

def read_todo():
    todo_id=input('id of item to read->')
    return get('http://127.0.0.1:5800/{}'.format(todo_id)).json()



print(add_todo())

print(read_todo())