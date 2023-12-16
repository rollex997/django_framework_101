#creation of the class
class Item:
    def calculate_total_price(self, price_, quantity_):
        return price_*quantity_
        
#Creating an instance of the class
item1 = Item() #class instance 1
item2 = Item() #class instance 2

#creating an attributes
#Hard coding Attribute1
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
#calling method from first instance of a class
result1 = item1.calculate_total_price(item1.price, item1.quantity)
print(f"total price of instance 1 = {result1}")
#Hard coding Attribute2
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 12
#calling method from second instance of a class
result2 = item2.calculate_total_price(item2.price, item2.quantity)
print(f"total price of instance 2 = {result2}")

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))

#How to create methods and execute them on our instances
random_str = "aaa"
print(random_str.upper())