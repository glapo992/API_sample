from flask import Flask, request
from flask_restful import Api, Resource

app=Flask(__name__)
api = Api(app)


class Helloworld(Resource): 
    """creation of a Resource extending Resource class form restful module"""
    def get(self):
        """name of the function is the same of the HTTP method. using get beacuse no datas are sent to this endpoint"""
        return{'Hello':'World'}
    


todos = {}

class TooSimple(Resource):
    def get(self, todo_id):
        return {todo_id : todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['note']
        return {todo_id : todos[todo_id]}



# correctly routing an api with restful package
api.add_resource(Helloworld, '/hello')
api.add_resource(TooSimple, '/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True, port=5800)