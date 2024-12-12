class Camera: 
    def __init__(self,clarity): 
        self.clarity=clarity 
    def display_camera(self): 
        print(f"Clarity:{self.clarity}") 
class Phone: 
    def __init__(self,types): 
        self.types=types 
    def display_phone(self): 
        print(f"Types:{self.types}") 
class Smartphone(Camera,Phone): 
    def __init__(self,clarity,types,brand,model): 
        Camera.__init__(self, clarity) 
        Phone.__init__(self, types) 
        self.brand=brand 
        self.model=model 
    def display_smartphone(self): 
        print(f"Clarity:{self.clarity}\nTypes:{self.types}\nBrand:{self.brand}\nModel:{self.model}") 
smart=Smartphone("hd","touch","APPLE","15 pro max") 
smart.display_smartphone()

class Student: 
    def __init__(self,name,course): 
        self.name=name 
        self.course=course 
    def display_student(self): 
        print(f"Name:{self.name}\nCourse:{self.course}") 
class Athlete(Student): 
    def __init__(self,name,course,sport): 
        super().__init__(name,course) 
        self.sport=sport 
    def display_athlete(self): 
        print(f"Sport:{self.sport}") 
s=Athlete("Poongu","AI","Basketball") 
s.display_student() 
s.display_athlete()  

_______________________________

class Vehicle: 
    def __init__(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year 
    def display(self): 
        print(f"Vehicle Make: {self.make}") 
        print(f"Vehicle Model: {self.model}") 
        print(f"Year: {self.year}") 
class Car(Vehicle): 
    def __init__(self, make, model, year, doors, trunk_capacity): 
        Vehicle.__init__(self,make, model, year) 
        self.doors = doors 
        self.trunk_capacity = trunk_capacity 
    def disp(self): 
        self.display() 
        print(f"Number of Doors: {self.doors}") 
        print(f"Trunk Capacity: {self.trunk_capacity} liters") 
class Truck(Vehicle): 
    def __init__(self, make, model, year, cargo_capacity, axles): 
        super().__init__(make, model, year) 
        self.cargo_capacity = cargo_capacity 
        self.axles = axles 
    def info(self): 
        self.display() 
        print(f"Cargo Capacity: {self.cargo_capacity} tons") 
        print(f"Number of Axles: {self.axles}") 
class PickupTruck(Car, Truck): 
    def __init__(self, make, model, year, doors, trunk_capacity, cargo_capacity, axles): 
        Car.__init__(self, make, model, year, doors, trunk_capacity) 
        Truck.__init__(self, make, model, year, cargo_capacity, axles) 
    def show(self): 
        self.disp() 
        print(f"Cargo Capacity: {self.cargo_capacity} tons") 
        print(f"Number of Axles: {self.axles}") 
make=input() 
model=input() 
year=int(input()) 
doors=int(input()) 
trunk_capacity=int(input()) 
cargo_capacity=int(input()) 
axles=int(input()) 
pickup = PickupTruck(make, model, year, doors, trunk_capacity, cargo_capacity, axles) 
pickup.show() 
 
 
class Product: 
    def __init__(self, product_id, name, price): 
        self.product_id = product_id 
        self.name = name 
        self.price = price 
    def info(self): 
        print(f"Product ID: {self.product_id}") 
        print(f"Product Name: {self.name}") 
        print(f"Price: {self.price} USD") 
class Electronics(Product): 
    def __init__(self, product_id, name, price, warranty_period, brand): 
        super().__init__(product_id, name, price) 
        self.warranty_period = warranty_period 
        self.brand = brand 
    def show(self): 
self.info() 
print(f"Warranty Period: {self.warranty_period} years") 
print(f"Brand: {self.brand}") 
class Clothing(Product): 
def __init__(self, product_id, name, price, size, material): 
super().__init__(product_id, name, price) 
self.size = size 
self.material = material 
def display_info(self): 
self.info() 
print(f"Size: {self.size}") 
print(f"Material: {self.material}") 
laptop = Electronics("E101", "Laptop", 1500, 2, "Dell") 
print("Electronics Details:") 
laptop.show() 
print("\n") 
shirt = Clothing("C202", "Shirt", 25, "L", "Cotton") 
print("Clothing Details:") 
shirt.display_info()






