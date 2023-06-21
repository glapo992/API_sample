# this is a very basic sample of API to use as reference
there are 2 exaples:
- raw flask api
- restful package
<hr>

### 1 flask api folder
run the server with flask
``` 
pyton3 flask_api/entry_point
```
in another terminal istance run:
```
python3 flask_api/request_sender
```
it asks you 2 inputs, sends them to the server and has it back changed
<hr>

### 2 REST api folder
run the server with flask
``` 
python3 REST_api/restful_api
```
in another terminal istance run:
```
pyton3 REST_api/req_to_restapi.py
```
prompt you to add a task and then print a todo list in stdout