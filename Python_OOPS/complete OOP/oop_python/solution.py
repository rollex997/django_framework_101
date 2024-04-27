# creating a class
class Phone:
    def __init__(self,brand,model,price,quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity
    def calulate_total_price(self):
        return self.price * self.quantity
    def calculate_gst(self):
        total_price = self.calulate_total_price()
        gst = total_price * (18/100)
        added_total_price_to_gst = total_price + gst
        return added_total_price_to_gst
#creating class instance
print("class Phone related stuff : ")
myphone = Phone("Motorolla","Razor",1500,3)
print(f"myphone brand = {myphone.brand}, myphone model = {myphone.model}")
print(f"myphone price = {myphone.price}, myphone quantity = {myphone.quantity}")
#calcualte total price
print(f" myphone calculate total price = {myphone.calulate_total_price()}")
print(f" myphone calculate gst price = {myphone.calculate_gst()}")
print("\n")

#inheritance
class SmartPhone(Phone):
    def __init__(self,brand,model,price,quantity,processor,ram,screen,battery):
        #using this super() we are accessing __init__ in the parent class so that we can insert values using constructor in the parent class
        super().__init__(brand,model,price,quantity)
        self.processor = processor
        self.ram = ram
        self.screen = screen
        self.battery = battery
# creating a class instance
print("class SmartPhone related stuff : (Inheritance)")
sp = SmartPhone("Samsung","GALAXY S24 Ultra",124000,1,"snap dragon 8 gen3", "16GB LPDDR4","6.7inch","2600mAH")
print(f"sp brand = {sp.brand}, sp model = {sp.model}, sp processor = {sp.processor},")
print(f"sp ram = {sp.ram}, sp screen = {sp.screen}, sp battery = {sp.battery}")
print(f"sp price = {sp.price}, sp quantity = {sp.quantity}")
print(f"sp calculate total price = {sp.calulate_total_price()}, sp calculate gst price = {sp.calculate_gst()}")
print("\n")

#encapsulation
'''
Now we want that users should not be able to access brand by using class object example
class_obj = Phone("Motorolla","Razor",1500,3)
print(class_obj.brand) --> output : Motorolla

first create a getter method to access the brand attribute and set the brand attribute to private
Making brand Private: self.__brand = brand
Get brand attribute using a getter method:
def get_brand(self):
    return self.__brand
example to get a private attribute and print it in the terminal
myphone = Phone("Motorolla","Razor",1500,3)
print(f"myphone brand = {myphone.get_brand()}, myphone model = {myphone.model}")
'''
class Phone:
    def __init__(self,brand,model,price,quantity):
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__quantity = quantity
    def get_brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand = brand

    def get_model(self):
        return self.__model
    def set_model(self,brand):
        self.__model = brand

    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price

    def get_quantity(self):
        return self.__quantity
    def set_quantity(self,quantity):
        self.__quantity = quantity

    def calulate_total_price(self):
        return self.__price * self.__quantity
    def calculate_gst(self):
        total_price = self.calulate_total_price()
        gst = total_price * (18/100)
        added_total_price_to_gst = total_price + gst
        return added_total_price_to_gst
print("class Phone related stuff : (Encapsulation)")
myphone = Phone("Motorolla","Razor",1500,3)
'''
If you change myphone.get_model() to myphone.model then you will get AttributeError: 'Phone' object has no attribute 'model'
'''
print(f"myphone brand = {myphone.get_brand()}, myphone model = {myphone.get_model()}")
print(f"-->trying to change brand using myphone.brand = 'Readme' <--")
myphone.brand = "lenovo"
print(f"myphone brand = {myphone.get_brand()}, myphone model = {myphone.get_model()}")
print(f"-->trying to change brand using myphone.__brand = 'Readme' <--")
myphone.__brand = "lenovo"
print(f"myphone brand = {myphone.get_brand()}, myphone model = {myphone.get_model()}")
print(f"-->trying to change brand using myphone.set_brand('Readme') <--")
myphone.set_brand("Readme")
myphone.set_model("Note10")
myphone.set_price(15000)
myphone.set_quantity(4)
print(f"myphone brand = {myphone.get_brand()}, myphone model = {myphone.get_model()}")
print(f"myphone price = {myphone.get_price()}, myphone quantity = {myphone.get_quantity()}")
#calcualte total price
print(f"myphone calculate total price = {myphone.calulate_total_price()}")
print(f"myphone calculate gst price = {myphone.calculate_gst()}")
print("\n")