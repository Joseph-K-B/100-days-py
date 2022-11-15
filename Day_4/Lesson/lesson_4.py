import random
import pi_module

"""
Pseudo random integers and floats
"""
# random_integer = random.randint(1, 10)
# print(random_integer)

# module import example #

# print(pi_module.pi)

# random float between 0-1 #

# random_float = random.random()
# print(random_float)

# random float between 0 - 4.9999... #

# random_float * 5

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

"""
Offsets & Appending items to Lists
"""

states_of_US = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]

# print(states_of_US[2])
# print(states_of_US[-1])

# states_of_US[1] = "Pencilvania"
states_of_US.append("Conneticut")
# print(states_of_US)

"""
IndexErrors & Working with Nested Lists
"""

# num_of_states = len(states_of_US)
# print(num_of_states - 1)

fruits = ["Strawberries", "Nectarines"]
vegetables = ["Spinach", "Kale"]

nested = [fruits, vegetables]
print(vegetables)