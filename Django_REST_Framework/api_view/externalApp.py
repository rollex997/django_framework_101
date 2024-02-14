# this app is used to test out our api's 
# this app is not related to the django app it's an external application
#client application
import requests
import json

'''create student'''
# data={
#     'name':'aditya',
#     'roll' : 150,
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
#     'name':'Barbatos',
#     'roll' : 117,
#     'city':'Rajasthan',
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/update_student/3'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.put(url=URL,data=json_data,headers=headers)
# print(request_.text)
'''update_student partial update'''
# data={
#     'city':'Lucknow',
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/update_student/3'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.put(url=URL,data=json_data,headers=headers)
# print(request_.text)

'''get one student record'''
# URL = 'http://127.0.0.1:8000/get_one_student/3'
# request_ = requests.get(url=URL)
# print(request_.text)

'''get all data'''
# URL = 'http://127.0.0.1:8000/get_all_student'
# request_ = requests.get(url=URL)
# print(request_.text)

'''delete student data from DB'''
# URL = 'http://127.0.0.1:8000/delete_student/3'
# headers = {'Content-Type':'application/json'}
# request_ = requests.delete(url=URL,headers=headers)
# print(request_.text)