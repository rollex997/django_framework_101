from item import Item
from phone import phone

# #instanciating Item class
# laptop1  = Item("lenovo yoga", 50000, 5)
# print(f"name : {laptop1.name_} quantity : {laptop1.quantity_} price : {laptop1.calculate_total_price()}")
# laptop2 = Item("jiobook", 17000, 7)
# print(f"name : {laptop2.name_} quantity : {laptop2.quantity_} price : {laptop2.calculate_total_price()}")

# print("\n")

# #instanciating phone class
# phone1_class_phone = phone("galaxy J", 14000, 5)
# print(f"name : {phone1_class_phone.name_} quantity : {phone1_class_phone.quantity_} price : {phone1_class_phone.calculate_total_price()}")
# phone2_class_phone = phone("iphone", 120000, 7)
# print(f"name : {phone2_class_phone.name_} quantity : {phone2_class_phone.quantity_} price : {phone2_class_phone.calculate_total_price()}")

# print("\n")

# print("Getting all the instances of Item and phone class")
# #getting all the instances of Item class
# print(Item.all_instanes_Item_class)
# #getting all the instances of phone class
# print(phone.all_phone_instances)

item1 = Item("MyItem", 750)
print(item1.name)
item1.name = "OtherItem"
print(item1.name)