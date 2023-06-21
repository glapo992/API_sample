"""sample of REST API with restful extension for flask """
from flask import Flask, request
from flask_restful import Api, Resource

app=Flask(__name__)
api = Api(app)


class Helloworld(Resource): 
    """creation of a Resource extending Resource class form restful module"""
    def get(self):
        """name of the function is the same of the HTTP method. using get beacuse no datas are sent to this endpoint"""
        return{'Hello':'World'}
    

# correctly routing an api with restful package
api.add_resource(Helloworld, '/hello')

#-----------------------------------------------------------
# creation of a TODO list where the key is a todo_id
# to test from terminal run:
# curl http://127.0.0.1:5800/todo_id_1 -d "note=Remember the milk" -X PUT -> insert item
# or
# curl http://127.0.0.1:5800/todo_id_1 -> display item inserted
todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        """returns the key:value pair of the corresponding ID """
        return {todo_id : todos[todo_id]}

    def put(self, todo_id):
        """allows to add new items to the dictionary """
        todos[todo_id] = request.form['note']
        return {todo_id : todos[todo_id]}


class DullClass1(Resource):
    def get(self):
        # return the dict and a response code (if not specified = 200) and a custom header 
        return {'key' : 'value'}, 201, {'Etag' : 'custom string'}

api.add_resource(TodoSimple, '/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True, port=5800)