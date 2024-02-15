from rest_framework.response import Response
from rest_framework.views import APIView
from class_based_api.models import Student
from class_based_api.serializers import StudentSerializers

class StudentAPI(APIView):
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Data created successfully!!'}, status=201)
        return Response({'status': serializer.errors}, status=500)

    def put(self, request):
        ID = request.data.get('ID')
        try:
            student = Student.objects.get(ID=ID)
            serializer = StudentSerializers(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'Data updated successfully!!!'}, status=200)
            return Response({'status': serializer.errors}, status=500)
        except Student.DoesNotExist:
            return Response({'status': 'Data does not exist'}, status=404)

    def get(self, request):
        ID=request.data.get("ID")
        if ID:
            try:
                student = Student.objects.get(ID=ID)
                serializer = StudentSerializers(student)
                return Response({'data':serializer.data},status=200)
            except Student.DoesNotExist:
                return Response({'status':'student does not exist'},status=400)
        else:   
           student = Student.objects.all()
           serializer = StudentSerializers(student, many=True)
           return Response({'data': serializer.data}, status=200)

    def delete(self, request):
        ID = request.data.get('ID')
        try:
            student = Student.objects.get(ID=ID)
            student.delete()
            return Response({'status': 'Data deleted successfully'}, status=204)
        except Student.DoesNotExist:
            return Response({'status': 'Data does not exist'}, status=400)
