import json
from django.http import JsonResponse
from django.shortcuts import render
from student.models import *

# Create your views here.
def student(request):
    title_ = 'Student'
    data = {'title' : title_}
    return render(request,'student/student.html',data)

def insert_student_info(request):
    is_ajax = request.headers.get('X-Requested-with') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            inserted_values = data.get('payload')
            Student_info.objects.create(name=inserted_values['name'],roll_no = inserted_values['roll_no'],mobile=inserted_values['mobile'],father_name=inserted_values['father_name'],mother_name=inserted_values['mother_name'],father_mobile=inserted_values['father_mobile'])
            print(inserted_values)
            return JsonResponse({'status':'student info added'},status=200)
        return JsonResponse({'status':'Invalid Request'},status=400)
    else:
        return JsonResponse({'status':'Error in request'},status=800)
    
def get_student_info(request):
    is_ajax = request.headers.get('X-requested-with') == 'XMLHttpRequest'
    if is_ajax:
        if request.method=='POST':
            data = list(Student_info.objects.all().values())
            return JsonResponse({'context':data},status=200)
        return JsonResponse({'status':'invalid request'},status=400)
    else:
        return JsonResponse({'message':'error in get data'},status=404)

def update_student_info(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            updated_values = data.get('payload')
            try:
                instance = Student_info.objects.get(pk=updated_values['student_ID'])
                print(instance)
                instance.name = updated_values['name']
                instance.roll_no = updated_values['roll_no']
                instance.mobile = updated_values['mobile']
                instance.father_name = updated_values['father_name']
                instance.mother_name = updated_values['mother_name']
                instance.father_mobile = updated_values['father_mobile']
                instance.save()
                return JsonResponse({'status':'Data Updated successfully'},status=200)
            except Student_info.DoesNotExist:
                return JsonResponse({'status':'record not found'},status=400)
        else:
            return JsonResponse({'status':'Invalid request method'},status=800)

def delete_student_info(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            deleted_value = data.get('payload')
            try:
                instance = Student_info.objects.get(pk=deleted_value['student_ID'])
                instance.delete()
                return JsonResponse({'status':'Data Deleted Successfully'},status=200)
            except Student_info.DoesNotExist:
                return JsonResponse({'status':'Record not found'},status=404)
        else:
            return JsonResponse({'status':'Invalid request method'},status=400)