# ➡️ Day 8: Introduction to Object-Oriented Programming (OOP)

Day 8 was a major step into modern programming paradigms. We learned about **Object-Oriented Programming**, a way to structure our code by creating our own custom data types using **classes** as blueprints.

* **Cheat Sheet:** [`day_8_cheatsheet.md`](./day8_cheatsheet.md)

---

### ⭐ Key Concepts Covered:

* **Classes and Objects:** Understanding the difference between a `class` (a blueprint) and an `object` (an actual instance created from the blueprint).
* **The `__init__()` Method:** A special "constructor" function that runs automatically when a new object is created to set up its initial state.
* **The `self` Keyword:** How an object refers to its own attributes and methods.
* **Attributes:** Variables that belong to an object and store its data (e.g., `player.name`).
* **Methods:** Functions that belong to an object and define its behavior (e.g., `player.take_damage()`).

---

### 💡 Highlight Snippet:

```python
# A class to represent a player in a game.
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = []

    def take_damage(self, amount):
        """Reduces the player's HP."""
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} takes {amount} damage! Current HP: {self.hp}")

# Creating an object (instance) from the class
player1 = Player("Arin")
player1.take_damage(25)
