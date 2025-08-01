# ➡️ Day 9: OOP and Inheritance

On Day 9, we built upon our OOP foundation by learning about **Inheritance**. This powerful concept allows us to create new "child" classes that reuse and extend the functionality of existing "parent" classes.

* **Cheat Sheet:** [`day_9_cheatsheet.md`](./day9_cheatsheet.md)

---

### ⭐ Key Concepts Covered:

* **Parent and Child Classes:** Creating a general parent class (e.g., `Pet`) and more specialized child classes (e.g., `Dog`, `Cat`) that inherit its properties.
* **The `super()` Function:** How a child class can call the `__init__` method of its parent to avoid rewriting setup code.
* **Adding Specialized Methods:** Giving child classes unique behaviors that the parent class doesn't have (e.g., a `.fetch()` method for a `Dog`).
* **`isinstance()`:** A function to check if an object is an instance of a specific class, allowing our program to behave differently for different types of objects.

---

### 💡 Highlight Snippet:

```python
# Parent Class
class Pet:
    def __init__(self, name):
        self.name = name

    def feed(self):
        print(f"{self.name} is eating.")

# Child Class that inherits from Pet
class Dog(Pet):
    def __init__(self, name):
        # Call the parent's __init__ method
        super().__init__(name)

    # Add a unique method
    def fetch(self):
        print(f"{self.name} fetches the ball!")

# The Dog object can use methods from both classes
my_dog = Dog("Fido")
my_dog.feed()  # Inherited from Pet
my_dog.fetch() # Unique to Dog
