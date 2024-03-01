#functions vs methods
'''
FUNCTIONS VS METHODS
functions are generally avalable for anyone to use 
methods are only accesible to objects of class inside of which that methods resides
functions are functions that is present outside the class
methods are a type of functions that are present inside of class
Len() --> way to call a function 
L.append() --> a way to call a method here L is the object of a class List
each and every variable in python is an object 
s = ""
type(s) -> will give of that it's of class string

    
    CONSTRUCTOR
    def __init__(self): --> is a special method called constructor, the code inside a constructor gets executed
     as soon as the object of a class is created
     unlike cunstructor in java in python the name of the constructor has to be __init__
     constructor is a magic methods
     You cannot create your own magic methods but you can use any of the pre-defined magic methods
     Magic methods don't need any object of a class to be able to use them you can call them using a class object but generally 
     It's not done 
     Magic methods gets called when a given criteria is satisfied on it's own and object of class can not call the magic methods
     what is the utility of a constructor method --> In a cosntructor you define your class's configurations
     that you don't want that the users of that particular class to be able to set manually. You want to set the configuration of that class
     as soon as the object of that class is created automatically
     (for example:
        -> connect with an internet connection
        -> using GPS
        -> connect to a database
     )

     CLASS OBJECTS
     How to create an object of a class:
     sbi = Atm() --> object_name = class_name() --> It will create the object of that class
     object is an instance of a class

     SELF
     self is an object print(id(self)) "It will generate the id of self" Now this is the address where the self is stored
     jis be class ke object ke saath aap currently kaam kar rahe ho vahi self hota hai
     sbi.create_pin() so sbi object here will passed as a self to the method called create_pin()
     if we remove self as an argument from a method of a class in python then the entire code crashes saying that the method accept 0 
     positional argument but 1 was given this happens because when we create an object of a class in python that object itself is passed in that 
     method as an argument in python
     Why we need self as an argument in the methods of a class?
     A class can only have data and methods
     Only a class object can access class's data and methods. In a class if there are two methods then both of them cannot access each other ,
     the only one who has the previlage to access the methods of a class is the object of that class. If in a class one method needs to 
     access another method then you can only do something like self.method_name() inside another method and self here is an object of the class
     har baar sbi self ban kar khud aa jaa raha hai and hence we are using self (sbi or the current object) to access methods in other methods.

     ENCAPSULATION
    To make your variables inside your class private you can add __variable infront of your variable.
    class Atm:
        def __init__(self):
            self.__pin = ""
            self.__balance = 0
            self.__menu()
        
        def __menu(self):
            pass
    you can still access the private variables in a class if you do something like this
    x = Atm()
    x.__Atm__balance
    Nothing in python is truely private. 
    Python is built for the adults not for kids. If a senior dev have written a variable that starts with double underscore then 
    It's a gentlemen's experience that a junior dev must not use that variable in a class constructor.

    when create object of a class like """sbi = Atm()""" Atm() is the real object of the class Atm and sbi is the variable that points to the 
     address of the actual object of Atm class in the memory. This sbi variable is called the reference variable.

     STATIC -->
     for example customer serial number must be static
     there are two types of variable one is instance variable and another is static variable
     instance variable --> 
     The value of instance variable is different for each object
     Sometimes you might need a variable whoes value for each object remains the same in this case it's the customer serial number
     This type of variable is called static or class ka variable
     another example of static variable is bank's IFSC code
     static variable is always defined outside the constructor
     instance variable is always defined inside the constructor
     when you want to access a static or a class variable then you access that using class name example
     class_name.static_variable_name (You don't even need to create an object of a class to access that static variable)
     whenever you want to access an instance variable then you use self to access that variable example : self.instance_variable_name
     NEED FOR STATIC VARIABLE
     static variable ki zarurat tab padti hai jab aapke saare objects ko shared kuch values chahiye hoti hai.
     STATIC METHODS 
     the methods that deal with the sattic variables in a class is called static methods
     static methods in a class do not require self object you can call a static method using your class name
      #static method
    @staticmethod
    def get_counter():
        return Atm.__counter
    #static method
    @staticmethod
    def set_counter(new_counter):
        if type(new_counter) == int:
            Atm.__counter=new_counter
            print(f"counter set {Atm.__counter}")
        else:
            print("wrong datatype")
    CALLING STATIC METHODS
    calling set_counter Atm.set_counter(5)  class_name.static_method_name()
    calling get_counter Atm.get_counter()   class_name.static_method_name(some_value)

    Relationships --> Aggregation (Has- A ) and Inheritance (IS - A)
    
'''
class Atm:

    #static variable / class variable
    __counter = 1
    def __init__(self):
        #instance variable
        self.__pin = ""
        self.__balance = 0
        self.serial_no = Atm.__counter
        Atm.__counter += Atm.__counter
        # self.__menu()
    #static method
    @staticmethod
    def get_counter():
        return Atm.__counter
    #static method
    @staticmethod
    def set_counter(new_counter):
        if type(new_counter) == int:
            Atm.__counter=new_counter
            print(f"counter set {Atm.__counter}")
        else:
            print("wrong datatype")
    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        if str(new_pin) == str:
            self.__pin = new_pin
            print("pin changed")
    def __menu(self):
        user_input = input("""
                           Hello how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2  to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposite()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.balance()
        else:
            print("program terminated")
    
    def create_pin(self):
        self.__pin = input("Enter your pin")
        print("pin set success")
    
    def deposite(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            amount = int(input("enter amount"))
            self.__balance = self.__balance + amount
            print("deposite function")
        else:
            print("invalid pin")

    def withdraw(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            amount = int(input("enter amount"))
            if amount<self.__balance:
                self.__balance = self.__balance-amount
                print("operation success")
            else:
                print("Insuffiencent funds")
        else:
            print("invalid pin")

    def check_balance(self):
        temp = input("enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")