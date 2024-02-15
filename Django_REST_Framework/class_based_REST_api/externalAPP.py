# this app is used to test out our api's 
# this app is not related to the django app it's an external application
#client application
import requests
import json

'''create student'''
# data={
#     'name':'czxzcx',
#     'roll' : 987798,
#     'city':'czxzcxx',
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/student_api'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.post(url=URL,data=json_data,headers=headers)
# print(request_.text)


'''update_student complete update'''
# data={
#     'ID':'1',
#     'name':'Barricade',
#     'roll' : 911,
#     'city':'Chennai',
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/student_api'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.put(url=URL,data=json_data,headers=headers)
# print(request_.text)
'''update_student partial update'''
# data={
#     'ID':'2',
#     'city':'Goa'
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/student_api'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.put(url=URL,data=json_data,headers=headers)
# print(request_.text)

'''get one student record'''
# data={
#     'ID':'2'
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/student_api'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.get(url=URL,data=json_data,headers=headers)
# print(request_.text)

'''get all data'''
# URL = 'http://127.0.0.1:8000/student_api'
# request_ = requests.get(url=URL)
# print(request_.text)

'''delete student data from DB'''
data={
    'ID' : 3
}
json_data = json.dumps(data)
URL = 'http://127.0.0.1:8000/student_api'
headers = {'Content-Type':'application/json'}
request_ = requests.delete(url=URL,data=json_data,headers=headers)
print(request_.text)