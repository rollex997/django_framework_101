from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from task1.models import *
from marks.models import *
from marks.serializers import *
from django.views.generic import TemplateView
from django.db import IntegrityError

# **** MARKS CRUD OPERATIONS STARTS ****
class MarksPage(TemplateView):
    template_name = 'Marks/marks.html'
class MarksCRUD_API(APIView):
    # Get one record or create new marks in database
    def post(self,request):
        id = request.data.get('marks_id')
        if id:
            #get one record of marks from DB
            try:
                marks = Marks.objects.get(id=id)
                serializer = MarksSerializers(marks)
                return Response({'status':200,'data':serializer.data},status=200)
            except Marks.DoesNotExist as e:
                return Response({'status':500,'error':str(e)},status=500)
        else:
            #create marks 
            serializer = MarksSerializers(data=request.data)
            try:
                if serializer.is_valid():
                    student = request.data['student']
                    serializer.save(student = student)
                    return Response({'status':201,'msg':'Marks Created'},status=201)
                else:
                    print(str(serializer.errors))
                    return Response({'status':500,'error':str(serializer.errors)},status=500)
            except IntegrityError as e:
                return Response({'status':500,'error':str(e)},status=500)
    # get all records of marks 
    def get(self, request):
        marks = Marks.objects.all()
        serializer = Get_All_MarksSerializers(marks, many=True)  # Query for instances of Marks
        if marks:  # You might want to check if there are any instances retrieved
            return Response({'status': 200, 'data': serializer.data}, status=200)
        else:
            return Response({'status': 500, 'error': 'Marks Not Found'}, status=500)
    #update marks 
    def put(self, request):
        student_id = request.data.get('student_id')
        try:
            student = Student.objects.get(id=student_id)
            marks = Marks.objects.get(student=student)
            serializer = MarksSerializers(instance=marks, data=request.data, partial=True)
            if serializer.is_valid():
                # Update the marks instance with the new data
                serializer.save()
                return Response({'status': 200, 'msg': 'Marks updated successfully'}, status=200)
            else:
                print(str(serializer.errors))
                return Response({'status': 400, 'error': str(serializer.errors)}, status=400)
        except Student.DoesNotExist as e:
            return Response({'status':400,'error':str(e)},status=400)
        except IntegrityError as e:
            return Response({'status':400,'error':str(e)},status=400)
    # delete marks data 
    def delete(self,request):
        marks_id = request.data.get('marks_id')
        try:
            marks_object = Marks.objects.get(id=marks_id)
            marks_object.delete()
            return Response({'status':200,'msg':'Marks Deleted'},status=200)
        except Marks.DoesNotExist as e:
            return Response({'status':400,'error':str(e)},status=400)
# **** MARKS CRUD OPERATIONS ENDS ****