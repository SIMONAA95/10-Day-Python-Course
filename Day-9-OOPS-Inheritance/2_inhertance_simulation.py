# ==========================================
# SECTION 1: The Parent Class - A General Blueprint
# ==========================================

print("SECTION 1: The Parent 'Pet' Class")
print("-" * 35)

# This is our PARENT class. It contains all the attributes and methods
# that are common to ALL pets.
class Pet:
    """A general class to represent a virtual pet."""
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.hunger = 50
        self.happiness = 50

    def __str__(self):
        return f"Pet Name: {self.name} ({self.animal_type})"

    def feed(self):
        """Reduces hunger and slightly increases happiness."""
        print(f"You feed {self.name}. Yum!")
        self.hunger -= 10
        if self.hunger < 0: self.hunger = 0

    def show_stats(self):
        """Displays the pet's current stats."""
        print(f"\n--- {self.name}'s Stats ---")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print("--------------------")

print("The parent Pet class has been defined.")
print("\n" + "="*50)

# ==========================================
# SECTION 2: Child Classes - Specialized Versions
# ==========================================

print("SECTION 2: Child Classes (Inheritance)")
print("-" * 40)

# A CHILD class inherits all the attributes and methods from its parent.
# The parent class is listed in parentheses after the child class name.

class Dog(Pet):
    # The Dog's __init__ method.
    def __init__(self, name):
        # super().__init__() calls the __init__ method of the parent class (Pet).
        # This is how we set up the name and animal_type that all pets have.
        super().__init__(name, "Dog")

    # This is a method that is UNIQUE to the Dog class.
    def fetch(self):
        print(f"{self.name} excitedly fetches the ball!")
        self.happiness += 15
        if self.happiness > 100: self.happiness = 100

class Cat(Pet):
    def __init__(self, name):
        # Call the parent's constructor
        super().__init__(name, "Cat")
        self.mood = "curious"

    # This is a method that is UNIQUE to the Cat class.
    def purr(self):
        print(f"{self.name} purrs contentedly.")
        self.happiness += 10
        if self.happiness > 100: self.happiness = 100

print("The specialized Dog and Cat child classes have been defined.")
print("\n" + "="*50)

# ==========================================
# SECTION 3: Day 9 Project - Running the Simulation
# ==========================================

print("SECTION 3: Running the Simulation")
print("-" * 35)

# --- Create a Specific Pet Object ---
while True:
    pet_choice = input("What kind of pet would you like? (dog/cat): ").lower()
    if pet_choice == "dog":
        pet_name = input("What will you name your dog? ")
        my_pet = Dog(pet_name)
        break
    elif pet_choice == "cat":
        pet_name = input("What will you name your cat? ")
        my_pet = Cat(pet_name)
        break
    else:
        print("Invalid choice. Please choose 'dog' or 'cat'.")

print(f"\nWelcome, {my_pet.name} the {my_pet.animal_type}!")


# --- The Main Game Loop ---
while True:
    my_pet.show_stats()
    
    print("\nWhat would you like to do?")
    print("1. Feed")
    # Dynamically show the special action based on the pet's class
    if isinstance(my_pet, Dog):
        print("2. Play fetch")
    elif isinstance(my_pet, Cat):
        print("2. Listen to purr")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        my_pet.feed() # This method is inherited from the Pet class!
    elif choice == "2":
        # isinstance() checks if an object is of a certain class.
        if isinstance(my_pet, Dog):
            my_pet.fetch() # This is the Dog's special method.
        elif isinstance(my_pet, Cat):
            my_pet.purr() # This is the Cat's special method.
    elif choice == "3":
        print(f"Goodbye! Take care of {my_pet.name}!")
        break
    else:
        print("Invalid choice.")

print("\n" + "="*50)
# print("Congratulations on completing Day 9! You've built a program using Inheritance.")
