from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
class adityaRateThrottle(UserRateThrottle):
    scope = 'aditya'