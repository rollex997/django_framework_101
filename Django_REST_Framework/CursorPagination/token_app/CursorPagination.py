from rest_framework.pagination import CursorPagination
class MyCursorPagination(CursorPagination):
    page_size=5 #number of records you want to see in one page
    ordering='name'