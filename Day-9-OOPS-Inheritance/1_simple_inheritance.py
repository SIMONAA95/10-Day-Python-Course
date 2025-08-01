# ==========================================
# SECTION 1: A Simpler Inheritance Example
# ==========================================

print("SECTION 2: A Simpler Inheritance Example")
print("-" * 40)

# Parent Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Moving forward!")

# Child Class
class Car(Vehicle): # Car inherits from Vehicle
    def honk(self):
        print("Beep beep!")

# Create an object of the child class
my_car = Car("Toyota")
print(f"My car is a {my_car.brand}.")
my_car.move() # This method was inherited from Vehicle
my_car.honk() # This method is unique to Car

print("\n" + "="*50)
