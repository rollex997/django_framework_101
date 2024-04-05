from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from task1.models import *
from task1.serializers import *
from django.views.generic import TemplateView,View
from django.db import IntegrityError
from marks.models import *
from marks.serializers import *

#generate pdf related imports
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table,TableStyle
from reportlab.lib import colors
import base64

# Create your views here.
class StudentDashboardView(TemplateView):
    template_name = 'task1/student_dashboard.html' 


# STUDENT DETAILS RELATED API/FUNCTIONS STARTS
class StudentDetailsView(TemplateView):
    template_name = 'task1/Student_details.html' 
class StudentAPI(APIView):
    def post(self,request):
        serializer = StudentSerializers(data = request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201,'msg':'Data Created Successfully!!!'},status=201)
            else:
                print(str(serializer.errors))
                return Response({'status':500,'error':str(serializer.errors)},status=500)
        except IntegrityError:
            return Response({'status':500,'error':'Roll number must be unique'},status=500)
    def put(self,request):
        id = request.data.get('id')
        try:
            student = Student.objects.get(id=id)
            serializer = StudentSerializers(student,data = request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'msg':'Data Updated!!'},status=200)
            else:
                print(str(serializer.errors))
                return Response({'status':500,'error':str(serializer.errors)},status=500)
        except Student.DoesNotExist as e:
            return Response({'status':404,'error':f"{e}"},status=404)
    def get(self,request,student_id=None):
        id = student_id
        if id:
            try:
                student = Student.objects.get(id=id)
                serializer = GetAllStudentSerializers(student)
                return Response({'status':200,'data':serializer.data},status=200)
            except Student.DoesNotExist as e:
                return Response({'status':400,'error':str(e)},status=400)
        else:
            #get all data
            student = Student.objects.all()
            serializer = GetAllStudentSerializers(student,many=True)
            return Response({'status':200,'data':serializer.data},status=200)
    def delete(self,request):
        id = request.data.get('id')
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return Response({'status':200,'msg':'Data Deleted'},status=200)
        except Student.DoesNotExist as e:
            return Response({'status':500,'error':e},status=500)
  # STUDENT DETAILS RELATED API/FUNCTIONS ENDS       
  
# STUDENT CATEGORY RELATED FUNCTIONS STARTS
class StudentCategoryPage(TemplateView):
    template_name = 'task1/student_category.html'
class StudentCategoryAPI(APIView):
    def post(self,request):
        serializer = StudentCategorySerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201,'msg':'Student Category Created'},status=201)
        else:
            print(str(serializer.errors))
            return Response({'status':500,'error':str(serializer.errors)},status=500)
    def get(self,request,category_id=None):
        id = category_id
        if id:
            try:
                student_category = StudentCategory.objects.get(id=id)
                serializer = StudentCategorySerializers(student_category)
                return Response({'status':200,'data':serializer.data},status=200)
            except StudentCategory.DoesNotExist as e:
                print(str(e))
                return Response({'status':400,'error':str(e)},status=400)
        else:
            student_category = StudentCategory.objects.all()
            serializer = StudentCategorySerializers(student_category,many=True)
            return Response({'status':200,'data':serializer.data},status=200)
    def put(self,request):
        id = request.data.get('category_id')
        if id:
            try:
                student_category = StudentCategory.objects.get(id=id)
                serializer = StudentCategorySerializers(student_category,data=request.data,partial=False)
                if serializer.is_valid():
                    print(serializer)
                    serializer.save()
                    return Response({'status':200,'msg':'Student category updated'},status=200)
                else:
                    print(str(serializer.errors))
                    return Response({'status':500,'error':str(serializer.errors)},status=500)
            except StudentCategory.DoesNotExist as e:
                return Response({'status':500,'error':str(e)},status=500)
        else:
            return Response({'status':500,'error':'Category id missing'},status=500)
    def delete(self,request):
        id=request.data.get('id')
        if id:
            student_category = StudentCategory.objects.get(id=id)
            try:
                student_category.delete()
                return Response({'status':200,'msg':'Data Deleted'},status=200)
            except StudentCategory.DoesNotExist as e:
                return Response({'status':400,'error':str(e)},status=400)
        else:
            return Response({'status':500,'error':'Record ID to Delete is not Found'},status=500)
# STUDENT CATEGORY RELATED FUNCTIONS ENDS  

# GET MARKS OF THE SELECTED STUDENT STARTS
student_id_backup=-1
class MarksCRUD_student_API(APIView):
    def get(self, request,student_id=None):
        # id = request.data.get('marks_id')
        id=student_id
        if id:
            student_id_backup=id
            #get one record of marks from DB
            try:
                marks = Marks.objects.get(student=id)
                serializer = MarksSerializers(marks)
                return Response({'status':200,'data':serializer.data},status=200)
            except Marks.DoesNotExist as e:
                return Response({'status':500,'error':str(e)},status=500)
        else:
            return Response({'status': 500, 'error': 'No Marks Selected'}, status=500)
# GET MARKS OF THE SELECTED STUDENT ENDS

# GENERATE DYNAMIC PDF AND DOWNLOAD IT IN YOUR DOWNLOADS FOLDER STARTS
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generate_pdf(request, student_id, categoryId, marks_id):
    if request.method == 'GET':
        # Retrieve data from the database
        student = Student.objects.get(id=student_id)
        student_category = StudentCategory.objects.get(id=categoryId)

        try:
            student_marks = Marks.objects.get(student=student_id)
    
            # Prepare data for the table
            marks_table_data = [
                ['Subject', 'Marks'],
                ['Maths', student_marks.maths],
                ['Physics', student_marks.physics],
                ['Chemistry', student_marks.chemistry],
                ['English', student_marks.english],
                ['Hindi', student_marks.hindi]
            ]
    
            # Create a PDF buffer
            buffer = io.BytesIO()
    
            # Create a PDF document
            pdf = SimpleDocTemplate(buffer, pagesize=letter)
    
            # Create a table and style
            marks_table = Table(marks_table_data)
            style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    
            marks_table.setStyle(style)
    
            # Add the table to the PDF document
            pdf.build([marks_table])
    
            # Get PDF data from the buffer
            pdf_data = buffer.getvalue()
    
            # Close the buffer
            buffer.close()
    
            # Return the PDF as a response
            return HttpResponse(pdf_data, content_type='application/pdf')
        except Marks.DoesNotExist as e:
            errors = str(e)
            return Response({'status':500,'error':errors},status=500)
# GENERATE DYNAMIC PDF AND DOWNLOAD IT IN YOUR DOWNLOADS FOLDER ENDS
