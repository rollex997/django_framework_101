from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from enroll.models import *
# Create your views here.
def enroll(request):
    Students = Student.objects.all()
    data = {'title' : 'Enroll', 'Student' : Students}
    return render(request,"enroll/enroll.html",data)
def get_all_data_api(request):
    
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            data = list(Student.objects.all().values())
            return JsonResponse({'context': data})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
