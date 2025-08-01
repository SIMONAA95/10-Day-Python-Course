# 🐍 Python Day 9 Cheat Sheet
## OOP and Inheritance

---

## 📝 Table of Contents
1. [Core Definitions](#-core-definitions)
2. [Basic Class Syntax](#-basic-class-syntax)
3. [Inheritance](#-inheritance)
4. [The `__str__` Method](#-the-str-method)
5. [The Main Application Loop](#-the-main-application-loop)
6. [Quick Reference](#-quick-reference)

---

## 🧠 Core Definitions

* **Class:** A blueprint for creating objects.
* **Object (Instance):** A specific item created from a class.
* **Attribute:** A variable that belongs to an object (e.g., `self.name`).
* **Method:** A function that belongs to an object (e.g., `self.bark()`).
* **Inheritance:** A way to form new classes using classes that have already been defined. This allows child classes to inherit the attributes and methods of parent classes.
* **Parent Class (or Superclass):** The class being inherited from.
* **Child Class (or Subclass):** The class that inherits from another class.
* **`super()`:** A special function that allows a child class to call methods from its parent class.

---

## 🏛️ Basic Class Syntax

```python
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def show_stats(self):
        print(f"Name: {self.name} | HP: {self.hp}")
```

---

## 👨‍👩‍👧‍👦 Inheritance

### Syntax
The child class name is followed by parentheses containing the parent class name.

```python
# Parent Class
class Pet:
    def __init__(self, name):
        self.name = name

    def feed(self):
        print(f"{self.name} is eating.")

# Child Class
class Dog(Pet): # Dog inherits from Pet
    def __init__(self, name, breed):
        # Call the parent's __init__ method to handle the 'name' attribute
        super().__init__(name)
        # Add a new attribute specific to the Dog class
        self.breed = breed

    # Add a method specific to the Dog class
    def bark(self):
        print("Woof!")

# Creating and using the child object
my_dog = Dog("Fido", "Golden Retriever")
my_dog.feed() # This method was INHERITED from the Pet class.
my_dog.bark() # This method is UNIQUE to the Dog class.
print(my_dog.breed) # Accessing a child-specific attribute.
```

---

## 📜 The `__str__` Method

Define this in your class to get a clean, readable output when you `print()` an object.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"

my_book = Book("The Hobbit", "J.R.R. Tolkien")
print(my_book) # Output: 'The Hobbit' by J.R.R. Tolkien
```

---

## 🕹️ The Main Application Loop

A common pattern for using your classes in an interactive program.

```python
# Create an object from your class
player1 = Player("Gandalf")

# Start an infinite loop for the menu
while True:
    choice = input("What do you do? (stats/quit): ")

    # Call the object's methods based on the input
    if choice == "stats":
        player1.show_stats()
    elif choice == "quit":
        print("Goodbye!")
        break
```

---

## ⚡ Quick Reference

| Concept | Syntax | Description |
| :--- | :--- | :--- |
| **Inheritance** | `class Child(Parent):` | `Child` gets all methods/attributes from `Parent`. |
| **Call Parent Method** | `super().method_name()` | Used inside a child class to call a parent's method. |
| **Check Object Type** | `isinstance(object, ClassName)` | Returns `True` if the object is an instance of the class. |
| **String Rep.** | `def __str__(self):` | Returns a string to be used when `print(object)` is called. |

---

*Happy coding! 🐍✨*
