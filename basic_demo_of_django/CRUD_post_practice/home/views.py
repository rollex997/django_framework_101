from django.http import JsonResponse
import json
from django.core.serializers import serialize
from django.shortcuts import redirect, render
from student.models import *
# Create your views here.
def home(request):
    title_ = "Home"
    data = {
        'title' : title_
    }
    return render(request,'home/home.html',data)
def get_Id(request,id):
    print (id)
    if id:
        return JsonResponse({'status':"ID recieved"},status=200)
    else:
        return JsonResponse({'status':'could not recieve any ID from student page/app'},status=404)
def get_data_by_ID(request):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            ID_from_student_app = data.get('payload')
            try:
                student_app_Db_instance = Student.objects.get(pk=ID_from_student_app['ID'])
                data = {
                    'name' : student_app_Db_instance.student_name,
                    'roll_no' : student_app_Db_instance.roll_no,
                    'mobile' : student_app_Db_instance.mobile,
                    'father_name' : student_app_Db_instance.father_name,
                    'mother_name' : student_app_Db_instance.mother_name,
                    'father_mobile' : student_app_Db_instance.father_mobile,
                }
                return JsonResponse({'context':data},status=200)
            except Student.DoesNotExist:
                return JsonResponse({'status':'Record does not exist'},status=404)
        else:
            return JsonResponse({'status':'invalid response'},status=400)
    else:
        return JsonResponse({'status':'response from frontend is null'},status=500)