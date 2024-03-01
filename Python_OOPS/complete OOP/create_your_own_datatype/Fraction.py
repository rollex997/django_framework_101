'''
    def __str__(self):
        return "hello"
    This is magic method that gets executed when you put the object of your class inside a print function
'''
class Fraction_class:
    def __init__(self,n,d):
        self.__num = n
        self.__den = d
    
    def __str__(self):
        return "{}/{}".format(self.__num,self.__den)
    def __add__(self,other):
        temp_num = (self.__num * other.__den) + (other.__num * self.__den)
        temp_den = self.__den * other.__den
        return "{}/{}".format(temp_num,temp_den)
    def __sub__(self,other):
        temp_num = (self.__num * other.__den) - (other.__num * self.__den)
        temp_den = self.__den * other.__den
        return "{}/{}".format(temp_num,temp_den)
    def __mul__(self,other):
        temp_num = self.__num * other.__num
        temp_den = self.__den * other.__den
        return "{}/{}".format(temp_num,temp_den)
    def __truediv__(self,other):
        temp_num = self.__num * other.__den
        temp_den = self.__den * other.__num
        return "{}/{}".format(temp_num,temp_den)