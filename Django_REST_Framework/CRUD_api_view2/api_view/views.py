from api_view.serializers import *
from api_view.models import *
from rest_framework.response import Response

#for auth, permission and rest api
from rest_framework.decorators import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# create / update data     
@api_view(['POST', 'PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def create_update_data(request):
    if request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Data inserted successfully!!!'}, status=401)
        else:
            return Response({'status': serializer.errors}, status=400)
    
    if request.method == 'PUT':
        ID = request.data.get('ID')
        try:
            student = Student.objects.get(ID=ID)
            serializer = StudentSerializers(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'Data is updated successfully!!'}, status=200)
            else:
                return Response({'status': serializer.errors}, status=400)
        except Student.DoesNotExist:
            return Response({'status': 'Student does not exist'}, status=404)

#Read one / read all data
@api_view(['GET','POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def read_all_one_data(request):
    if request.method=='POST':
        ID = request.data.get('ID')
        try:
            student=Student.objects.get(ID=ID)
            serializer = StudentSerializers(student)
            return Response({'data':serializer.data},status=200)
        except Student.DoesNotExist:
            return Response({'status':'Data does not exist'})
    if request.method=='GET':
        student = Student.objects.all()
        serializer = StudentSerializers(student,many=True)
        return Response({'data':serializer.data},status=200)

# delete data 
@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_data(request):
    if request.method=='POST':
        ID = request.data.get('ID')
        try:
            student=Student.objects.get(ID=ID)
            student.delete()
            return Response({'status':'Data is deleted successfully!!!'},status=200)
        except Student.DoesNotExist:
            return Response({'status':'Student Does not exist'},status=404)