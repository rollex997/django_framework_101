from django.http import JsonResponse
import json
from django.shortcuts import render
from enroll.models import *
# Create your views here.
def enroll(request):
    title = "Enroll"
    data = {'title':title}
    return render(request,"enroll/enroll.html",data)
def insert_data(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    #Student.objects.create(name=inserted_values['name'],mobile=inserted_values['mobile'],city=inserted_values['city'],roll_number=inserted_values['roll_no'])
    #creates record in DB
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            inserted_values = data.get('payload')
            Student.objects.create(name=inserted_values['name'],mobile=inserted_values['mobile'],city=inserted_values['city'],roll_number=inserted_values['roll_no'])
            return JsonResponse({'status': 'student added!'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return JsonResponse({'status': 'Error in request'}, status=800)

def get_data(request):
        
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    #Student.objects.all().values() gets all the records from DB
    if is_ajax:
        if request.method == 'GET':
            data = list(Student.objects.all().values())
            return JsonResponse({'context': data},status=200)
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return JsonResponse({'message' : 'Error in Insertion'},status=400)

def update_data(request):
     # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('payload')
            try:
                #Student.objects.get(pk=updated_values['SID']) = Fetches only one record from DB
                instance = Student.objects.get(pk=updated_values['SID'])
                instance.name = updated_values['name']
                instance.mobile = updated_values['mobile']
                instance.city = updated_values['city']
                instance.roll_number = updated_values['roll_no']
                instance.save()
                return JsonResponse({'status': 'Data updated successfully'})
            except Student.DoesNotExist:
                return JsonResponse({'status': 'Record not found'}, status=4)
    else:
        return JsonResponse({'status': 'Invalid request method'}, status=400)

def delete_data(request):
     # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'PUT':
            data = json.load(request)
            updated_values = data.get('payload')
            try:
                #Student.objects.get(pk=updated_values['SID']) = Fetches only one record from DB
                instance = Student.objects.get(pk=updated_values['SID'])
                instance.delete()
                return JsonResponse({'status': 'Data Deleted successfully'})
            except Student.DoesNotExist:
                return JsonResponse({'status': 'Record not found'}, status=4)
    else:
        return JsonResponse({'status': 'Invalid request method'}, status=400)