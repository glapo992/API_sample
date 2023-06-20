import requests
import json

rand_str = "text container 2"

url = "http://localhost:5500/process_text"  #ip address and the open port of the server target

response = requests.post(url=url, data=rand_str)
print(response.text)


class Person:
	"""dull class to test how to send obj between containers
	"""
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname


name = "Ciro"
surname = "Mariano"
person = Person(name = name, surname=surname) #istance of the object
json_p = json.dumps(person.__dict__) #automatically creates a dict from person obj with all the attr
url_p = "http://localhost:5500/person"  #ip address of the server target
headers = {"Content-Type":"application/json"}
response = requests.post(url=url_p, data=json_p, headers=headers)
print (response.text)

