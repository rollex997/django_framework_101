from django.http import JsonResponse
import json
from django.shortcuts import render
from student.models import *
# Create your views here.
def student(request):
    title_ = "Student"
    data = {
        'title' : title_
    }
    return render(request, 'student/student.html',data)

def insert_student_info(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            inserted_values = data.get('payload')
            print(inserted_values)
            Student.objects.create(
                  student_name=inserted_values['student_name'],
                  roll_no=inserted_values['roll_no'],
                  mobile=inserted_values['mobile'],
                  father_name=inserted_values['father_name'],
                  mother_name=inserted_values['mother_name'],
                  father_mobile=inserted_values['father_mobile'],
                  )
            return JsonResponse({'status' : 'Data Created successfully!!'},status=200)
        else:
            return JsonResponse({'status' : 'Invalid Request'},status=400)
    else:
        return JsonResponse({'status' : 'Error in request'},status = 404)

def Read_student_info(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = list(Student.objects.all().values())
            return JsonResponse({'context':data},status=200)
        else:
            return JsonResponse({'messege' : 'Invalid Request'},status=400)
    else:
        return JsonResponse({'messege' : 'Error in getting data'},status=404)

def Update_student_info(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method=='POST':
            data = json.load(request)
            updated_values = data.get('payload')
            try:
                database_instance = Student.objects.get(pk=updated_values['student_ID'])
                print(database_instance)
                database_instance.student_name = updated_values['student_name']
                database_instance.roll_no = updated_values['roll_no']
                database_instance.mobile = updated_values['mobile']
                database_instance.father_name = updated_values['father_name']
                database_instance.mother_name = updated_values['mother_name']
                database_instance.father_mobile = updated_values['father_mobile']
                database_instance.save()
                return JsonResponse({'status' : 'Data Updated Successfully'},status=200)
            except Student.DoesNotExist:
                return JsonResponse({'status':'data not found'},status=404)
        else:
            return JsonResponse({'status':'Invalid request'},status=400)

def delete_student_info(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            deleted_data = data.get('payload')
            try:
                database_instance = Student.objects.get(pk=deleted_data['student_ID'])
                print(database_instance)
                database_instance.delete()
                return JsonResponse({'messege':'data deleted successfully'},status=200)
            except Student.DoesNotExist:
                return JsonResponse({'messege':'Data not found in the database'},status=404)
        else:
            return JsonResponse({'messege':'invalid request'},status=400)
