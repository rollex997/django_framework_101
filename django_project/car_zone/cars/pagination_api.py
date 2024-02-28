from rest_framework import pagination
class MyPagination(pagination.PageNumberPagination):
    page_size=8
    #allow client to define page size and query parameter
    page_size_query_param='records'
    max_page_size = 8
    # last_page_strings='end'
    '''
    http://127.0.0.1:8000/cars_api/cars/?page=1&records=1
    '''

class FeaturedCarsPagination(pagination.PageNumberPagination):
    page_size=3
    page_size_query_param='records'
    max_page_size=8
'''
http://127.0.0.1:8000/cars_api/featured_cars/
'''

class LatestCarPagination(pagination.PageNumberPagination):
    page_size=6
    page_size_query_param = 'records'
    max_page_size = 8
'''
http://127.0.0.1:8000/cars_api/latest_cars/
'''