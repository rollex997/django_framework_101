# this app is used to test out our api's 
# this app is not related to the django app it's an external application
#client application
import requests
import json

'''create student'''
# data={
#     'name':'Dyson',
#     'roll' : 100,
#     'city':'Kanpur',
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/create_update_student'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.post(url=URL,data=json_data,headers=headers)
# print(request_.text)


'''update_student complete update'''
# data={
#     'Student_ID':'8',
#     'name':'Leo',
#     'roll' : 7,
#     'city':'Bangaluru',
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/create_update_student'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.put(url=URL,data=json_data,headers=headers)
# print(request_.text)
'''update_student partial update'''
# data={
#     'Student_ID':'8',
#     'name':'LightFury'
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/create_update_student'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.put(url=URL,data=json_data,headers=headers)
# print(request_.text)

'''get one student record'''
# data={
#     'Student_ID':'5'
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/get_one_all_student'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.post(url=URL,data=json_data,headers=headers)
# print(request_.text)

'''get all data'''
# URL = 'http://127.0.0.1:8000/get_one_all_student'
# request_ = requests.get(url=URL)
# print(request_.text)

'''delete student data from DB'''
# data={
#     'Student_ID' : 9
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/delete_student'
# headers = {'Content-Type':'application/json'}
# request_ = requests.post(url=URL,data=json_data,headers=headers)
# print(request_.text)