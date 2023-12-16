#creation of the class
class Item:
    #create a list of instances that will hold all the instances of a class
    all_instanes = []
    #creating a class attribute:
    pay_rate = 0.8 #pay rate after 20% discount

    def __init__(self, name : str, price: float, quantity=0):
        #run validations to the recieved arguments in the constructor
        assert price >=0, f"Price {price} is not greater than zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than zero!"
        #Assign to self object
        print(f"An instance of class for {name} is created")
        self.name_ = name
        self.price_ = price
        self.quantity_ = quantity

        #append the instance as soon as it's created
        #self is acutally instance itself every time that is being created.
        Item.all_instanes.append(self)
    def calculate_total_price(self):
        return self.price_*self.quantity_
    def apply_discount(self):
        self.price_ = self.price_ * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name_}', '{self.price_}', '{self.quantity_}')"
        
#Creating an instance of the class
item1 = Item("Phone", 100,1) #class instance 1
item2 = Item("Laptop", 1000,3) #class instance 2
item3 = Item("Cable", 10,5) #class instance 3
item4 = Item('Mouse', 50,5) #class instance 4
itme5 = Item("Keyboard", 75,5) #class instance 5

print(Item.all_instanes)

for instance in Item.all_instanes:
    print(instance.name_)