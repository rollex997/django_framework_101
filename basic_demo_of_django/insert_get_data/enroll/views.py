from pickletools import long1
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

    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            data = data.get('payload')
            Student.objects.create(name=data['name'],mobile=data['mobile'],city=data['city'],roll_number=data['roll_no'])
            return JsonResponse({'status': 'student added!'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return JsonResponse({'status': 'Error in request'}, status=800)

def get_data(request):
        
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            data = list(Student.objects.all().values())
            return JsonResponse({'context': data},status=200)
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return JsonResponse({'message' : 'Error in Insertion'},status=400)