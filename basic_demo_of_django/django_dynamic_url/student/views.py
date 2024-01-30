from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
import json
from student.models import *
from marks.models import *
# Create your views here.
def student(request):
    title_ = 'Student'
    data = {
        'title' : title_
    }
    return render(request,'student/student.html',data)

def insert_student_data(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data=json.load(request)
            inserted_values = data.get('payload')
            Student.objects.create(
                 Student_Name = inserted_values['Student_Name'],
                 Father_Name = inserted_values['Father_Name'],
                 roll_no = inserted_values['roll_no'],
                 mobile = inserted_values['mobile'],
                 email = inserted_values['email'],
            )
            print(f"data insert : {inserted_values}")
            return JsonResponse({'status':'data insert successfull'},status=200)
        else:
            return JsonResponse({'status' : 'Error in request'},status=400)
    else:
        return JsonResponse({'status':'something went wrong no ajax request'},status=500)

def read_student_data(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            data = list(Student.objects.all().values())
            return JsonResponse({'context' : data},status=200)
        else:
            return JsonResponse({'status':'Invalid request'},status=400)
    else:
        return JsonResponse({'status' : 'Error in get data'},status=404)

def update_student_data(request):
    is_ajax = request.headers.get("X-Requested-With") == ('XMLHttpRequest')
    if is_ajax:
        if request.method == "POST":
            data = json.load(request)
            updated_value = data.get('payload')
            print(updated_value)
            try:
                Student_DB_instance = Student.objects.get(pk=updated_value['student_ID'])
                print(Student_DB_instance)
                Student_DB_instance.Student_Name = updated_value['Student_Name']
                Student_DB_instance.Father_Name = updated_value['Father_Name']
                Student_DB_instance.roll_no = updated_value['roll_no']
                Student_DB_instance.mobile = updated_value['mobile']
                Student_DB_instance.email = updated_value['email']
                Student_DB_instance.save()
                return JsonResponse({'status' : 'Data updated successfully!!!'},status=200)
            except Student.DoesNotExist:
                return JsonResponse({'status':'record not found'},status=404)
        else:
            return JsonResponse({'status':'invalid response'},status=400)
    else:
        return JsonResponse({'status':'ajax post is not present'},status=500)

def delete_student_data(request):
    is_ajax = request.headers.get('X-Requested-With')=="XMLHttpRequest"
    if is_ajax:
        if request.method=="POST":
            data=json.load(request)
            deleted_value = data.get('payload')
            print(deleted_value['student_ID'])
            try:
                Student_DB_instance = Student.objects.get(pk=deleted_value['student_ID'])
                print(f"{Student_DB_instance.Student_Name} , {Student_DB_instance.student_ID} deleted")
                Student_DB_instance.delete()
                return JsonResponse({'status':'Data Deleted successfully'},status=200)
            except Student.DoesNotExist:
                return JsonResponse({'status':'Record not found'},status=404)
        else:
            return JsonResponse({'status':'Invalid Request'},status=400)
    else:
        return JsonResponse({'status':'ajax not found'},status=500)
    

# student details page starts
def student_details(request):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    if is_ajax:
        if request.method=='POST':
            data = json.load(request)
            student_detail = data.get('payload')
            ID = student_detail['student_ID']
            print(f"student_details function studentID = {ID}")
            return JsonResponse({'status':'Id recieved'},status=400)
        else:
            return JsonResponse({'status':'invalid request'},status=400)
        
def student_details_page(request,ID):
    if ID:
        Student_DB_instance = Student.objects.get(pk=ID)
        try:
            Student_Marks = Marks.objects.get(Student_ID = ID)
            marks_settings = MarksSettings.objects.first()
            passing_percentage = marks_settings.passing_percentage
            Total_marks_per_subject = marks_settings.Total_marks_per_subject
            Total_Marks = Total_marks_per_subject*6
            data = {
                    'student_ID' : Student_DB_instance.student_ID,
                    'Student_Name' : Student_DB_instance.Student_Name,
                    'Father_Name' : Student_DB_instance.Father_Name, 
                    'roll_no' : Student_DB_instance.roll_no, 
                    'mobile' : Student_DB_instance.mobile,
                    'email' : Student_DB_instance.email,
                    
                    'Maths' : Student_Marks.Maths,
                    'Physics' : Student_Marks.Physics,
                    'Chemistry' : Student_Marks.Chemistry,
                    'Computer' : Student_Marks.Computer,
                    'English' : Student_Marks.English,
                    'Hindi' : Student_Marks.Hindi,
                    'Total_marks_obtained' : Student_Marks.Total_marks_obtained,
                    'Total_Marks' : Total_Marks,
                    'Percentage' : Student_Marks.Percentage,
                    'passing_percentage' : passing_percentage,
                    'pass_fail' : Student_Marks.pass_fail,
            }
            print(data)
            return render(request,'student/student_details.html',data)
        except Marks.DoesNotExist:
            print("marks does not exist")
            Student_DB_instance = Student.objects.get(pk=ID)
            data = {
                    'student_ID' : Student_DB_instance.student_ID,
                    'Student_Name' : Student_DB_instance.Student_Name,
                    'Father_Name' : Student_DB_instance.Father_Name, 
                    'roll_no' : Student_DB_instance.roll_no, 
                    'mobile' : Student_DB_instance.mobile,
                    'email' : Student_DB_instance.email,
            }
            return render(request,'student/student_details.html',data)
    
# student details page ends