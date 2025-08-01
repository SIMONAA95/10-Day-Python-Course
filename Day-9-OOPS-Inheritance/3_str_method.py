# ===================================================
# SECTION 3: STR Method - Controlling print()ing an object.
# ===================================================


class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

# Without a __str__ method
my_pet = Pet("Fido", "Dog")
print(my_pet) 
# Output will be something ugly like: <__main__.Pet object at 0x10a5f4e50>


class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
    
    # This is the special method
    def __str__(self):
        return f"Pet Name: {self.name} ({self.animal_type})"

# With a __str__ method
my_pet = Pet("Fido", "Dog")
print(my_pet)
# Output is now clean and readable: Pet Name: Fido (Dog)
