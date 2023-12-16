#creation of the class
class Item:
    #creating a class attribute:
    pay_rate = 0.8 #pay rate after 20% discount
    def __init__(self, name : str, price: float, quantity=0):
        #run validations to the recieved arguments in the constructor
        assert price >=0, f"Price {price} is not greater than zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than zero!"
        #Assign to self object
        print(f"An instance of class for {name} is created")
        self.price_ = price
        self.quantity_ = quantity
    def calculate_total_price(self):
        return self.price_*self.quantity_
    def apply_discount(self):
        self.price_ = self.price_ * self.pay_rate
        
#Creating an instance of the class
item1 = Item("Phone", 100,12) #class instance 1
item2 = Item("Laptop", 1000,4) #class instance 2

#calling method from first instance of a class
result1 = item1.calculate_total_price()
print(f"total price of instance 1 = {result1}")

#calling method from second instance of a class
result2 = item2.calculate_total_price()
print(f"total price of instance 2 = {result2}")

# accessing class attribute:
print(f"class attribute pay rate : {Item.pay_rate}")
#accessing class attribute from a class instances item1 and item2 
print(f"class attribute pay rate : {item1.pay_rate}")
print(f"class attribute pay rate : {item2.pay_rate}")

#this will bring you all the attribute that are associated to this class at class level
print(f"attributes associated to Item class CLASS LEVEL: {Item.__dict__}")
#this  will bring you all the attribute that are associated to this class at instance level
print(f"attributes associated to Item class INSTANCE LEVEL: {item1.__dict__}")

item3 = Item("Phone", 5000, 1)
result3 = item3.apply_discount()
print(f"discount : {item3.price_} payrate_class_level= {item3.pay_rate}")

#if you want to change the discount amount for the laptop without changing the class attribute of discount amount then
item4 = Item("Laptop", 40000, 3)
item4.pay_rate = 0.7
result4 = item4.apply_discount()
print(f"the discount for the laptop is {item4.price_} payrate_instance level : {item4.pay_rate}")