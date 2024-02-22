from rest_framework.pagination import PageNumberPagination
class MyPageNoPagination(PageNumberPagination):
    # page_size=5
    page_query_param = 'page'
    #allow client to define page size and query parameter
    page_size_query_param='records'
    max_page_size = 7
    last_page_strings='end'