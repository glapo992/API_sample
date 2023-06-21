"""sample of REST API with restful extension for flask """
from flask import Flask, request
from flask_restful import Api, Resource, abort

app=Flask(__name__)
api = Api(app)


class Helloworld(Resource): 
    """creation of a Resource extending Resource class form restful module"""
    def get(self):
        """name of the function is the same of the HTTP method. using get beacuse no datas are sent to this endpoint"""
        return{'Hello':'World'}
    


api.add_resource(Helloworld, '/hello') # correctly routing an api with restful package

#-----------------------------------------------------------
# creation of a TODO list where the key is a todo_id
# to test from terminal run:
# curl http://127.0.0.1:5800/todo_id_1 -d "note=Remember the milk" -X PUT -> insert item
# or
# curl http://127.0.0.1:5800/todo_id_1 -> display item inserted
todos = {}

class TodoSimple(Resource):
    def get(self, todo_id:str)->dict:
        """returns the key:value pair of the corresponding ID """
        if todo_id not in todos: #error message if the ID doesnt exist
            abort(404, message="Todo {} doesn't exist".format(todo_id))
        return {todo_id : todos[todo_id]}
    
    def delete(self, todo_id:str)->dict:
        """delete the correspondig values from the dict"""
        if todo_id not in todos:
            abort(404, message="Todo {} doesn't exist".format(todo_id))
        del todos[todo_id]
        return '', 204 # returns a custom http message

    def put(self, todo_id:str)->dict:
        """adds new items to the dictionary """
        todos[todo_id] = request.form['note']
        return {todo_id : todos[todo_id]}

api.add_resource(TodoSimple, '/todo-simple/<string:todo_id>')


#----------------------------------------
# manage subtask in dict and POST request

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}



class TodoList(Resource):
    def get(self):
        return TODOS


    def post(self):
        """post request and auto generation of todo_id"""
        todo_id = int(max(TODOS.keys()).lstrip('todo')) +1
        todo_id = 'todo%i' %todo_id
        data = request.get_json() 
        TODOS[todo_id] = data


        
        return TODOS[todo_id], 201

api.add_resource(TodoList, '/todos')



class DullClass1(Resource):
    def get(self):
        # return the dict and a response code (if not specified = 200) and a custom header 
        return {'key' : 'value'}, 201, {'Etag' : 'custom string'}

if __name__ == '__main__':
    app.run(debug=True, port=5800)