import requests
import json

rand_str = "text container 2"

url = "http://localhost:5500/process_text"  #ip address and the open port of the server target
# send a hard coded string and have it back modified
response = requests.post(url=url, data=rand_str)
print(response.text)


class Person:
	"""dull class to test how to send obj between applications
	"""
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname


def send_request(person):
    json_p = json.dumps(person.__dict__) #automatically creates a dict from person obj with all the attr
    url_p = "http://localhost:5500/person"  #ip address and endpoint of the server target
    headers = {"Content-Type":"application/json"}
    response = requests.post(url=url_p, data=json_p, headers=headers)
    return response



name = input('give him a name-> ')
surname = input('and a surname-> ')
person = Person(name = name, surname=surname) #istance of the object 
given_surname = person.surname


response = send_request(person=person)
print (response)

print('{}, but before I was known as {} {}'.format(response.text,person.name, given_surname))