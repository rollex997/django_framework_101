#pass by reference
'''
In python everything is object hence if you pass an object of Customer class in this case then the behavior of your class object
will be the same.

what is pass by reference?
a = 3
b = a
in this case a will point to the address of 3 and b will also point to the same address 3 

in python class objects are also mutable (dictionary, list and sets)
change(L1[:]) --> this is how you do cloning 
now the List that is sent in the fucntion change It will be a duplicate List sent to the function change
hence making your list immutable

in python tuple is immutable
https://youtu.be/Mf2RdpEiXjU?t=7829

start video from here
https://youtu.be/Mf2RdpEiXjU?t=7898
'''
# class Customer:
#     def __init__ (self,name, gender):
#           self.gender = gender
#           self.name = name
# def greet(customer):
#      if customer.gender == "Male":
#           print("Hello sir",customer.name)
#      if customer.gender == "Female":
#           print("Hello madam",customer.name)
# cust = Customer("Aditya","Male")
# cust2 = Customer("Aastha","Female")
# greet(cust)
# greet(cust2)
'''
 collection of objects
 when you loop through the object then you can do a it like you do a normal loop

 this code will not work on sets becasue in sets only immutable datat types can go 
 but in objects mutable data type can go


'''
# class Customer:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def intro(self):
#         print(f"I am {self.name} and I am {self.age}")

# c1 = Customer("Aditya",27)
# c2 = Customer("Aastha",26)
# c3 = Customer("Ayushi",25)
# L = [c1,c2,c3]
# for i in L:
#     i.intro()

'''
AGGREGATION
cutomer class yaha pe address class ke change_address method se kaam karva raha hai address change karne ke liye
isi relation ko ham aggregation kehte hai

'''
# class Customer:
#     def __init__(self,name,gender,address):
#         self.name = name
#         self.gender = gender
#         self.address = address
#     def edit_profile(self,new_name,new_city,new_pin,new_state):
#         self.name = new_name
#         self.address.change_address(new_city,new_pin,new_state)
# class Address:
#     def __init__(self,city,pincode,state):
#         self.city = city
#         self.pincode = pincode
#         self.state = state
#     def change_address(self,new_city,new_pin,new_state):
#         self.city = new_city
#         self.pincode = new_pin
#         self.state = new_state

# add=Address("Kolkata",268859,"WB")
# cust=Customer("Aditya","Male",add)
# cust.edit_profile("Akaash","gurgaon","111","Haryana")
# print(cust.address.city)
