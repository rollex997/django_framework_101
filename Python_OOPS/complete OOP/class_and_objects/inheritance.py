'''
INHERITANCE
Inheritance allows us to reuse are code in another class (Code resuability)
parent class --> child class
child class can inherit from parent class
parent class cannot inherit child class
when you inherit a class then what do you inherit?
1. all variables gets inherited by the child classes
2. all methods gets inherited by the child classes
3. constructor gets inherited by the child classes
4. private members are not inherited by the child classes

If there is no constructor in child class and the parent class has a constructor then 
when you create an object of a child class then the constructor of the parent class will automatically get executed

If there is a constructor present in the child and parent class then the constructor of the child class will get executed instead of the parent
class

POLYMORPHISM HAVE 
1. METHOD OVERRIDING
METHOD OVERRIDING (POLYMORPHISM)
if parent and child classes have a method that has the same name then when you create an object of the child class 
and call that method the method of the child class will be called this is called method overriding
2. METHOD OVERLOADING
ek hi method me alag alag inputs de ke alag alag behavior induce karva sakte ho
in python method overloading technically speaking kaam nai karti hai
https://youtu.be/Mf2RdpEiXjU?t=12984
3. OPERATOR OVERLOADING
operator overloading is achieved using magic methods like __add__(self):

SUPER KEYWORD:
What is Super?
super().parent_method_name() --> we use super to invoke (call) the methods in our parent class inside our child classes
super keyword doesn't work outside the child class
using super keyword you can access
1. parent class methods 
2. parent class cosntructor
3. you cannot access the attributes of the parent class
https://youtu.be/Mf2RdpEiXjU?t=11525    
Uses of a super keyword
super keyword allows you to use the parent class attributes that are common in your child class
super().__init__() should be your firs statement in your class methods otherwise it won't work
https://youtu.be/Mf2RdpEiXjU?t=11679

Types of inheritance in Python
1. SINGLE LEVEL INHERITANCE 
parent class --> child class
2. MULTI LEVEL INHERITANCE
grandparent class  --> parent class --> child class
3. HIRERACHAL INHERITANCE
one parent and multiple children
4. MULTIPLE INHERITANCE
one child 2 parents (In java This type of inheritance is not present)
5. HYBRID INHERITANCE
https://youtu.be/Mf2RdpEiXjU?t=12362

MRO (Method resolution order)
https://youtu.be/Mf2RdpEiXjU?t=12633
'''
class User:
    def login(self):
        print("Login")
    def register(self):
        print("resgister")
class Student(User):
    def enroll(self):
        print("enroll")
    def review(self):
        print("review")
stu = Student()
stu.enroll()
stu.review()
stu.login()
stu.register()