from flask import Flask, request

app = Flask (__name__)


class Person:
	"""dull class to test how to send obj between containers
	"""
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
	
	def __str__(self) -> str:
		return "hi, I am {} {} :)".format(self.name, self.surname)


#---------ENDPOINTS-------------------------------------

@app.route("/process_text", methods=['POST']) 
def process_text():
	"""basic example of api accepting a string and return it concatenate with another one. 
	it is reachable at the endpoint <this ip addr>/process_text
	"""
	data = request.get_data(as_text = True) # accepts the request from http protocol and post it back
	result = data + " text container 1"
	return result


@app.route("/person", methods=['POST']) 
def person():
	"""endpoint who recives a json (serialyzed form person obj in the other node) and translate into a Person obj, returns the __str__ method of Person.

	:return: __str__ method
	:rtype: str
	"""
	p_data        :dict   = request.get_json() 
	person        :Person = Person(name=p_data['name'], surname=p_data['surname'])
	person.surname:str    = "de Carli"
	result        :str    = person.__str__()  #this is a string

	return result 


if __name__== "__main__":
	app.run(port=5500,debug=True) 
	#the ip of the guest must be specified (in this case the ip of this specific container). 
	#if the ip is not known, put "0.0.0.0"-> listen on all nework interfaces availabe on the container 	#app.run(host='0.0.0.0', port=5000,debug=True)
	#if the ip is not specified, it goes by default to localhost, so it is reachable only from this self container
