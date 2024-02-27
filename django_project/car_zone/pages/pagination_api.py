from rest_framework.pagination import PageNumberPagination
class MyPageNoPagination(PageNumberPagination):
   # page_size=5 # no of records per page
   page_query_param = 'page'
   #allow client to define page size and query parameter
   page_size_query_param='records'
   max_page_size = 5
   last_page_strings='end'
