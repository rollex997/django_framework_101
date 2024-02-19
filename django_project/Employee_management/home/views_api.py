from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from auth_api.models import EmployeeProfile
@api_view(['POST'])
def homepage_api(request):
    if request.user.is_authenticated:
        user = request.user
        employee_profile = EmployeeProfile.objects.get(user=user)
        data={
            'username':user.username,
            'email':user.email,
            'phone':employee_profile.phone
        }
        return Response({'user':data},status=200)
    else:
        return Response({'status':404},status=404) #user not found