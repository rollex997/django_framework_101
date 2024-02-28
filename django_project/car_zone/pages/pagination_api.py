from rest_framework.pagination import PageNumberPagination
class MyPageNoPagination(PageNumberPagination):
    page_size=3
    page_query_param = 'page'
    #allow client to define page size and query parameter
    page_size_query_param='records'
    max_page_size = 7
    # last_page_strings='end'
    '''
    your url should look something like this
    http://127.0.0.1:8000/pages_api/teams/?page=1&records=1
    '''