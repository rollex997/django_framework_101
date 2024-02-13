# this app is used to test out our api's 
# this app is not related to the django app it's an external application
#client application
import requests
import json
# create student
# data={
#     'name':'Ballistic',
#     'roll' : 1000,
#     'city':'Udaipur',
# }
# json_data = json.dumps(data)
# URL = 'http://127.0.0.1:8000/create_student'
# headers = {'Content-Type': 'application/json'}
# request_ = requests.post(url=URL,data=json_data,headers=headers)
# print(request_)


# update_student
data={
    'Student_ID':'2',
    'name':'aastha kumar',
    'roll' : 69,
    'city':'Lucknow',
}
json_data = json.dumps(data)
URL = 'http://127.0.0.1:8000/update_student'
headers = {'Content-Type': 'application/json'}
request_ = requests.post(url=URL,data=json_data,headers=headers)
print(request_.text)