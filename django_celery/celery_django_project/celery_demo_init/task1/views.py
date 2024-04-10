from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from task1.models import *
from task1.serializers import *
from django.views.generic import TemplateView,View
from django.db import IntegrityError
from marks.models import *
from marks.serializers import *

# generate pdf from html page dynamically related imports
from task1.pdf import *
from django.shortcuts import HttpResponse

#related to pdf send via email import 
from django.core.files.base import ContentFile
#email backend
from django.core.mail import EmailMessage

#celery related imports 
#tasks imports 
from task1.tasks import *
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

# generate pdf from html page dynamically starts
# backup data for pdf generation
student_marks_backup = {}
student_backup = {}
student_category_backup = {}
class pdf_page_caller(APIView):
    def get(self,request,student_id, categoryId, marks_id):
        try:
            student = Student.objects.get(id=student_id)
            student_category = StudentCategory.objects.get(id=categoryId)
            student_marks = Marks.objects.get(id=marks_id)
            # Save these Db objects in a dictionary for backup
            student_marks_backup.clear()
            student_backup.clear()
            student_category_backup.clear()
            student_marks_backup['student_marks'] = student_marks
            student_backup['student'] = student
            student_category_backup['student_category'] = student_category
            return Response({'status': 200, 'msg': 'open pdf'}, status=200)
        except Student.DoesNotExist as e:
            return Response({'status': 500, 'error': str(e)}, status=500)
        except StudentCategory.DoesNotExist as e:
            return Response({'status': 500, 'error': str(e)}, status=500)
        except Marks.DoesNotExist as e:
            return Response({'status': 500, 'error': str(e)}, status=500)

def pdf_page(request):
    data = {
        'student':student_backup['student'],
        'student_category':student_category_backup['student_category'],
        'student_marks':student_marks_backup['student_marks'],
    }
    pdf = html2pdf('task1/pdf_page.html',data)
    student_marks_backup.clear()
    student_backup.clear()
    student_category_backup.clear()
    return HttpResponse(pdf,content_type='application/pdf')

# CELERY WORKER RELATED PROGRAM STARTS
# SEND PDF USING EMAIL (USING CELERY) STARTS
class send_PDF_via_Email_using_celery(APIView):
    def post(self, request):
        try:
            student_id = request.data['student_id']
            categoryId = request.data['categoryId']
            marks_id = request.data['marks_id']
            student = Student.objects.get(id=student_id)
            student_category = StudentCategory.objects.get(id=categoryId)
            if marks_id:
                student_marks = Marks.objects.get(id=marks_id)
                # Generate PDF content
                data = {
                    'student': student,
                    'student_category': student_category,
                    'student_marks': student_marks,
                }
                pdf_content = html2pdf('task1/pdf_page.html', data)
                
                if pdf_content:
                    # Save PDF content temporarily
                    # temp_pdf = ContentFile(pdf_content.getvalue())
                    temp_pdf_name = f'{student.name}_report.pdf'  # Set a filename
                    
                    # Send PDF via email (you can use the email sending logic here)
                    email_id = 'aryan268859@gmail.com'  # Replace with recipient's email
                    subject = f"Report for {student.name}"
                    message = f"Attached is the report for {student.name}."
                    # email = EmailMessage(subject, message, to=[email_id])
                    # email.attach(temp_pdf.name, temp_pdf.read(), 'application/pdf')
                    # email.send()
                    send_email_task.delay(email_id,subject,message,temp_pdf_name,pdf_content.getvalue())
    
                    return Response({'status': 200, 'msg': 'PDF sent successfully'}, status=200)
                else:
                    return Response({'status': 500, 'error': 'Failed to generate PDF'}, status=500)
            else:
                return Response({'status':500,'error':'Marks Not found'},status=500)
        except (Student.DoesNotExist, StudentCategory.DoesNotExist, Marks.DoesNotExist) as e:
            return Response({'status': 500, 'error': str(e)}, status=500)
# SEND PDF USING EMAIL (USING CELERY) ENDS
# CELERY WORKER RELATED PROGRAM ENDS
# generate pdf from html page dynamically ends
