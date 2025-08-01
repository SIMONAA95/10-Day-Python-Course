# 🐍 The Ultimate Python Beginner's Cheat Sheet

This document is a comprehensive reference for the core concepts covered in the 10-Day Beginner Python Course.

---

## 📝 Table of Contents
1.  [The Basics (Day 1 & 2)](#-the-basics-day-1--2)
2.  [Data Collections (Day 3)](#-data-collections-day-3)
3.  [Loops (Day 4)](#-loops-day-4)
4.  [Functions (Day 5)](#-functions-day-5)
5.  [Modules (Day 6)](#-modules-day-6)
6.  [File I/O (Day 7)](#-file-io-day-7)
7.  [Object-Oriented Programming (OOP) (Day 8 & 9)](#-object-oriented-programming-oop-day-8--9)
8.  [Bonus Concepts (Day 10)](#-bonus-concepts-day-10)
9.  [Real-World Application Map](#-real-world-application-map)
10. [Remembering Tips & Mnemonics](#-remembering-tips--mnemonics)
11. [Common Mistakes to Avoid](#-common-mistakes-to-avoid)
12. [Useful Websites & Next Steps](#-useful-websites--next-steps)

---

## 基礎 The Basics (Day 1 & 2)

### Printing, Variables, and Input
```python
# Print a message to the screen
print("Hello, World!")

# Store information in a variable
message = "Python is fun!"
print(message)

# Get input from the user (always returns a string)
name = input("What is your name? ")
print(f"Hello, {name}!") # f-string for easy formatting
```

### Data Types
* **`str` (String):** Text, e.g., `"Hello"`, `'Python'`.
* **`int` (Integer):** Whole numbers, e.g., `10`, `-5`.
* **`float` (Float):** Decimal numbers, e.g., `3.14`, `-0.5`.
* **`bool` (Boolean):** `True` or `False`.

### Type Conversion
You must convert strings to numbers for math.
```python
age_string = input("Enter your age: ") # e.g., user types "25"
age_number = int(age_string) # age_number is now the integer 25

price_string = input("Enter the price: ") # e.g., user types "9.99"
price_number = float(price_string) # price_number is now the float 9.99
```

### Conditionals (`if`/`elif`/`else`)
Making decisions in your code.
```python
age = 20
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```
**Comparison Operators:** `==` (equal), `!=` (not equal), `>`, `<`, `>=`, `<=`

---

## 🗂️ Data Collections (Day 3)

| Type | Syntax | Ordered? | Changeable? | Duplicates? | Use Case |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **List** | `[1, 2, 3]` | Yes | Yes | Yes | General-purpose, ordered sequence. |
| **Tuple** | `(1, 2, 3)` | Yes | No | Yes | Data that should not change (safer). |
| **Set** | `{1, 2, 3}` | No | Yes | No | Storing unique items, fast membership tests. |
| **Dictionary**| `{'a': 1}`| Yes* | Yes | No (Keys)| Storing key-value pairs. |
*\*Ordered in Python 3.7+*

### Key Operations
```python
# List
my_list = ["apple", "banana"]
my_list.append("cherry") # Add to end
my_list[0] = "avocado"   # Change item
del my_list[1]           # Remove by index

# Dictionary
my_dict = {"name": "Alex", "level": 5}
my_dict["level"] = 6       # Change value
my_dict["xp"] = 100        # Add new key-value pair
del my_dict["name"]        # Remove by key

# Set
my_set = {1, 2, 3}
my_set.add(4)              # Add item
my_set.remove(2)           # Remove item
```

---

## 🔁 Loops (Day 4)

### `for` Loop
Iterates over a sequence.
```python
# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop a specific number of times with range()
for i in range(5): # Loops from 0 to 4
    print(i)
```

### `while` Loop
Repeats as long as a condition is true.
```python
count = 1
while count <= 5:
    print(count)
    count += 1 # IMPORTANT: Increment the counter to avoid an infinite loop!
```

### Loop Control
* **`break`:** Exits the current loop immediately.
* **`continue`:** Skips the rest of the current iteration and moves to the next one.

---

## 📦 Functions (Day 5)

### Defining and Calling
```python
# Define a function with parameters
def greet(name, time_of_day):
    print(f"Good {time_of_day}, {name}!")

# Call the function with arguments
greet("Alice", "morning")
```

### `return` vs. `print`
* `print`: Shows a value to the user. The program cannot use this value.
* `return`: Sends a value back from the function to the code that called it. This allows the program to use the result.

```python
def add(a, b):
    return a + b # Sends the result back

# Catch the returned value in a variable
sum_result = add(5, 3)
print(f"The result is {sum_result}") # The result is 8
```
**Remembering Tip:** Variables created inside a function are **local** and disappear when the function ends. `return` is the only way to get a value out.

---

## 🧰 Modules (Day 6)

### Importing and Using
```python
# Import the entire module
import random
roll = random.randint(1, 6)

# Import a specific function
from math import sqrt
root = sqrt(16) # No "math." prefix needed

# Import with an alias (nickname)
import datetime as dt
now = dt.datetime.now()
```

---

## 💾 File I/O (Day 7)

### Reading and Writing
The `with` statement is the safest way to handle files as it closes them automatically.
```python
# Writing to a file ('w' mode erases existing content)
with open('data.txt', 'w') as f:
    f.write("Hello, file!\n")

# Appending to a file ('a' mode adds to the end)
with open('data.txt', 'a') as f:
    f.write("This is a new line.\n")

# Reading from a file ('r' mode)
with open('data.txt', 'r') as f:
    contents = f.read()
    print(contents)
```
**Remembering Tip:** Use `os.path.exists('filename')` to check if a file exists before trying to read it to prevent errors.

---

## 🏛️ Object-Oriented Programming (OOP) (Day 8 & 9)

### Classes and Objects
* **Class:** A blueprint for creating objects (e.g., `class Dog:`).
* **Object:** An instance of a class (e.g., `my_dog = Dog()`).

```python
class Player:
    # The constructor, runs when a new object is created
    def __init__(self, name):
        # Attributes: data that belongs to the object
        self.name = name
        self.hp = 100

    # Method: a function that belongs to the object
    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} took {amount} damage!")

# Create an object (instance)
player1 = Player("Arin")
player1.take_damage(20) # Call the object's method
```

### Inheritance
Create a child class that inherits all attributes and methods from a parent class.
```python
# Parent Class
class Pet:
    def __init__(self, name):
        self.name = name

# Child Class
class Cat(Pet):
    def __init__(self, name):
        super().__init__(name) # Call the parent's constructor

    def purr(self):
        print(f"{self.name} purrs.")

my_cat = Cat("Whiskers")
my_cat.purr() # Method from Cat class
```

---

## ✨ Bonus Concepts (Day 10)

### List Comprehensions
A concise, "Pythonic" way to create lists.
```python
# The long way
squares = []
for i in range(5):
    squares.append(i * i)

# The short way
squares = [i * i for i in range(5)] # [0, 1, 4, 9, 16]
```

### JSON
The standard way to save complex data structures (like dictionaries and lists) to files.
```python
import json

data = {"name": "Alex", "inventory": ["sword", "shield"]}

# Save data to a file
with open('save.json', 'w') as f:
    json.dump(data, f, indent=4)

# Load data from a file
with open('save.json', 'r') as f:
    loaded_data = json.load(f)
```

---

## 🌎 Real-World Application Map

* **Variables & Printing:** Displaying a username and score in a game.
* **Input & Conditionals:** A login form that checks if a password is correct.
* **Data Collections:** A social media profile (dictionary) with a list of friends (list).
* **Loops:** An e-commerce site calculating the total of your shopping cart by looping through the prices.
* **Functions:** A `send_email()` function that can be called from many different parts of an application without rewriting the code.
* **Modules:** A weather app importing a module to get weather data instead of calculating it from scratch.
* **File I/O:** A game saving your progress to a file so you can load it later.
* **OOP:** A banking application where each `Account` is an object with its own balance (attribute) and can perform actions like `deposit()` (method).

---

## 💡 Remembering Tips & Mnemonics

* **DRY Principle:** **D**on't **R**epeat **Y**ourself. If you're writing the same code multiple times, it's time to use a loop or a function.
* **Functions vs. Classes:** Functions are **verbs** (actions, like `calculate_tax`). Classes are **nouns** (things, like `Player` or `Car`).
* **`print` vs. `return`:** `print` is for **humans** to see. `return` is for the **program** to use.
* **File Modes:**
    * `'r'` is for **R**eading.
    * `'w'` is for **W**riting (and will **W**ipe out the file).
    * `'a'` is for **A**ppending (adding to the end).
* **Data Structures:**
    * **L**ist: A **L**ine of items. (Ordered)
    * **T**uple: A **T**ouch-proof list. (Unchangeable)
    * **S**et: Only **S**ingular items. (Unique)
    * **D**ictionary: A **D**efinition for each word. (Key-Value)

---

## 🎯 Common Mistakes to Avoid

* **`=` vs. `==`:** A single equals (`=`) is for assigning a value to a variable. A double equals (`==`) is for comparing if two things are equal.
* **Forgetting `int()` or `float()`:** `input()` always gives you a string. You can't do math with it until you convert it.
* **Infinite `while` Loops:** Always make sure the condition in your `while` loop will eventually become `False`.
* **Forgetting `self`:** Every method inside a class must have `self` as its first parameter.
* **Forgetting to Call a Function:** Writing `my_function` doesn't run it. You need to write `my_function()`.
* **Indentation Errors:** Python is very strict about indentation. All code inside a block (like an `if` statement, loop, or function) must be indented consistently.

---

## 🌐 Useful Websites & Next Steps

* **Practice & Challenges:**
    * [LeetCode](https://leetcode.com/): Great for interview-style coding problems.
    * [HackerRank](https://www.hackerrank.com/): Offers challenges and skill certification.
    * [Codewars](https://www.codewars.com/): Fun, martial-arts themed challenges.
* **Documentation & Learning:**
    * [Official Python Documentation](https://docs.python.org/3/): The ultimate source of truth.
    * [Real Python](https://realpython.com/): High-quality tutorials on a huge range of topics.
* **What to Learn Next:**
    * **Web Development:** Flask, Django
    * **Game Development:** Pygame
    * **Data Science:** Pandas, NumPy, Matplotlib
    * **Automation:** BeautifulSoup, Selenium
