from rest_framework.pagination import LimitOffsetPagination
class MyLimitOfSetPagination(LimitOffsetPagination):
    default_limit = 3 # page size or number of records
    max_limit = 5 # max allowable records that can be requested by the client
    
