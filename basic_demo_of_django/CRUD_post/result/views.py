from django.shortcuts import render
import json
from django.http import JsonResponse
from result.models import *
# Create your views here.
def result(request):
    title = "results"
    data = {
        'title' : title
    }
    return render(request, 'result/result.html',data)
def total_marks_fun(science, math ,computerScience):
    total_marks_ = science + math + computerScience
    return total_marks_
def percentage_fun(total_marks, totalMarksPerSubject):
    percentage = (total_marks / totalMarksPerSubject) * 100
    return percentage
def insert_marks(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            inserted_values = data.get('payload')
            #get the respective student from Student_info model in Student application
            Student_info_instance = Student_info.objects.get(pk=inserted_values['student_ID'])
            total_marks = total_marks_fun(float(inserted_values['science']) , float(inserted_values['math']) , float(inserted_values['computerScience']))
            percentage = percentage_fun(total_marks , float(inserted_values['totalMarksPerSubject']))
            flag=False
            if(percentage >= float(inserted_values['passingPercentage'])):
                flag=True
            else:
                flag=False
            marks.objects.create(
                 student=Student_info_instance,
                 student_name=inserted_values['student_name'],
                 science=inserted_values['science'],
                 math=inserted_values['math'],
                 computerScience=inserted_values['computerScience'],
                 Total_marks_per_subject=float(inserted_values['totalMarksPerSubject']),
                 Total_obtained_marks=total_marks,
                 percentage=percentage,
                 passingPercentage=inserted_values['passingPercentage'],
                 pass_fail=flag
                                 )
            print(inserted_values)
            return JsonResponse({'status':'Student marks added successfully!!'},status=200)
        return JsonResponse({'status':'Invalid request'},status=400)
    else:
        return JsonResponse({'status':'error in request'},status=800)
    
def get_marks(request):
    is_ajax = request.headers.get('X-Requested-With') ==  "XMLHttpRequest"
    if is_ajax:
        if request.method =='POST':
            data = list(marks.objects.all().values())
            print(data)
            return JsonResponse({'context' : data},status=200)
        return JsonResponse({'status':'invalid request'},status=400)
    else:
        return JsonResponse({'messege':'error in get data'},status=404)
    
def update_marks(request):
    is_ajax = request.headers.get('X-Requested-With') == "XMLHttpRequest"
    if is_ajax:
        if request.method == "POST":
            data = json.load(request)
            updated_values = data.get('payload')
            try:
                # Student_info_instance = Student_info.objects.get(pk=updated_values['student_ID'])
                instance = marks.objects.get(pk=updated_values['marks_ID'])
                print(instance)
                total_marks = total_marks_fun(float(updated_values['science']) , float(updated_values['math']) , float(updated_values['computerScience']))
                percentage = percentage_fun(total_marks , float(updated_values['totalMarksPerSubject']))
                flag=False
                if(percentage >= float(updated_values['passingPercentage'])):
                    flag=True
                else:
                    flag=False
                # instance.student = Student_info_instance
                instance.science = updated_values['science']
                instance.math = updated_values['math']
                instance.computerScience = updated_values['computerScience']
                instance.Total_marks_per_subject = updated_values['totalMarksPerSubject']
                instance.Total_obtained_marks=total_marks
                instance.percentage=percentage
                instance.passingPercentage = updated_values['passingPercentage']
                instance.pass_fail=flag
                instance.save()
                return JsonResponse({'status':'Data Updated successfully'},status=200)
            except marks.DoesNotExist:
                return JsonResponse({'status':'record not found'},status=404)
        else:
            return JsonResponse({'status':'Invalid Request'},status=800)
def delete_marks(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        data = json.load(request)
        deleted_value = data.get('payload')
        try:
            instance = marks.objects.get(pk=deleted_value['marks_ID'])
            instance.delete()
            return JsonResponse({'status':'Data Deleted Successfully'},status=200)
        except marks.DoesNotExist:
            return JsonResponse({'status':'Record not found'},status=404)
    else:
        return JsonResponse({'status':'Invalid Request'},status=800)