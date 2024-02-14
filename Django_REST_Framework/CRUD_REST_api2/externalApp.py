# this app is used to test out our api's 
# this app is not related to the django app it's an external application
#client application
import requests
import json

'''create student'''
# data={
#     'name':'Aditya',
#     'roll' : 1,
#     'city':'Kanpur',
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/create_student'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.post(url=URL,data=json_data,headers=headers)
# print(request_.text)
'''create student and also send an image file to the backend'''
'''TODO'''

'''update_student complete update'''
# data={
#     'Student_ID':'2',
#     'name':'Barricade',
#     'roll' : 747,
#     'city':'Kochi',
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/update_student'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.post(url=URL,data=json_data,headers=headers)
# print(request_.text)
'''update_student partial update'''
# data={
#     'Student_ID':'2',
#     'city':'Karnataka',
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/update_student'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.post(url=URL,data=json_data,headers=headers)
# print(request_.text)

'''get one student record'''
# data={
#     'Student_ID':'2'
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/get_one_student'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.post(url=URL,data=json_data,headers=headers)
# print(request_.text)

'''get all data'''
# URL = 'http://127.0.0.1:8000/get_all_student'
# request_ = requests.post(url=URL)
# print(request_.text)

'''delete student data from DB'''
# data={
#     'Student_ID' : 3
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/delete_student'
# headers = {'Content-Type':'application/json'}
# request_ = requests.post(url=URL,data=json_data,headers=headers)
# print(request_.text)