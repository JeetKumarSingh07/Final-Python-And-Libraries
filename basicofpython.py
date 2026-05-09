# ============================================================
# PYTHON BASICS - COMPLETE REFERENCE
# ============================================================


# ------------------------------------------------------------
# 1. PRINT & COMMENTS
# ------------------------------------------------------------
print("Hello, World!")       # Single-line comment
# This is also a comment

"""
This is a
multi-line comment (docstring)
"""


# ------------------------------------------------------------
# 2. VARIABLES & DATA TYPES
# ------------------------------------------------------------
x = 10              # int
y = 3.14            # float
name = "Alice"      # str
is_active = True    # bool
nothing = None      # NoneType

# Type checking
print(type(x))      # <class 'int'>

# Type conversion
print(int("5"))     # 5
print(float(3))     # 3.0
print(str(100))     # "100"
print(bool(0))      # False


# ------------------------------------------------------------
# 3. STRINGS
# ------------------------------------------------------------
s = "Hello, Python!"

print(s.upper())            # HELLO, PYTHON!
print(s.lower())            # hello, python!
print(s.replace("Python", "World"))  # Hello, World!
print(s.split(", "))        # ['Hello', 'Python!']
print(s[0:5])               # Hello  (slicing)
print(len(s))               # 15
print(s.strip())            # removes whitespace
print("py" in s)            # False (case-sensitive)

# f-strings (formatted strings)
age = 25
print(f"My name is {name} and I am {age} years old.")


# ------------------------------------------------------------
# 4. OPERATORS
# ------------------------------------------------------------
# Arithmetic
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...
print(10 // 3)  # 3  (floor division)
print(10 % 3)   # 1  (modulus)
print(10 ** 3)  # 1000 (exponent)

# Comparison
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 3)    # True
print(5 < 3)    # False
print(5 >= 5)   # True

# Logical
print(True and False)   # False
print(True or False)    # True
print(not True)         # False


# ------------------------------------------------------------
# 5. USER INPUT
# ------------------------------------------------------------
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))


# ------------------------------------------------------------
# 6. CONDITIONAL STATEMENTS
# ------------------------------------------------------------
num = 10

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Ternary (one-liner)
result = "Even" if num % 2 == 0 else "Odd"
print(result)


# ------------------------------------------------------------
# 7. LOOPS
# ------------------------------------------------------------

# for loop
for i in range(5):          # 0 1 2 3 4
    print(i, end=" ")
print()

for i in range(1, 10, 2):   # 1 3 5 7 9
    print(i, end=" ")
print()

# while loop
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# break & continue
for i in range(10):
    if i == 5:
        break               # stops loop
    if i % 2 == 0:
        continue            # skips even numbers
    print(i, end=" ")       # 1 3
print()


# ------------------------------------------------------------
# 8. LISTS
# ------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]

print(fruits[0])            # apple
print(fruits[-1])           # cherry (last item)
fruits.append("mango")      # add to end
fruits.insert(1, "grape")   # insert at index
fruits.remove("banana")     # remove by value
fruits.pop()                # remove last item
print(len(fruits))          # length
print(fruits[1:3])          # slicing
fruits.sort()               # sort in place
print(fruits)

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)              # [1, 4, 9, 16, 25]


# ------------------------------------------------------------
# 9. TUPLES
# ------------------------------------------------------------
coords = (10, 20, 30)       # immutable (can't change)
print(coords[0])            # 10
print(len(coords))          # 3
a, b, c = coords            # unpacking
print(a, b, c)              # 10 20 30


# ------------------------------------------------------------
# 10. DICTIONARIES
# ------------------------------------------------------------
person = {
    "name": "Alice",
    "age": 25,
    "city": "Delhi"
}

print(person["name"])           # Alice
print(person.get("age"))        # 25
person["email"] = "a@test.com"  # add key
person["age"] = 26              # update key
del person["city"]              # delete key

print(person.keys())            # all keys
print(person.values())          # all values
print(person.items())           # key-value pairs

# Loop through dict
for key, value in person.items():
    print(f"{key}: {value}")


# ------------------------------------------------------------
# 11. SETS
# ------------------------------------------------------------
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s1.add(5)
s1.remove(1)

print(s1 | s2)   # union
print(s1 & s2)   # intersection
print(s1 - s2)   # difference


# ------------------------------------------------------------
# 12. FUNCTIONS
# ------------------------------------------------------------
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))

# Default parameters
def power(base, exp=2):
    return base ** exp

print(power(3))     # 9
print(power(3, 3))  # 27

# *args and **kwargs
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))  # 10

def show_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

show_info(name="Alice", age=25)

# Lambda function
square = lambda x: x ** 2
print(square(5))  # 25


# ------------------------------------------------------------
# 13. SCOPE
# ------------------------------------------------------------
x = "global"

def my_func():
    x = "local"     # local scope
    print(x)        # local

my_func()
print(x)            # global


# ------------------------------------------------------------
# 14. EXCEPTION HANDLING
# ------------------------------------------------------------
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No error occurred")
finally:
    print("This always runs")

# Raise an exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


# ------------------------------------------------------------
# 15. FILE HANDLING
# ------------------------------------------------------------
# Write to file
with open("test.txt", "w") as f:
    f.write("Hello, File!\n")
    f.write("Second line\n")

# Read from file
with open("test.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())

# Append to file
with open("test.txt", "a") as f:
    f.write("Appended line\n")


# ------------------------------------------------------------
# 16. CLASSES & OBJECTS (OOP)
# ------------------------------------------------------------
class Animal:
    # Class variable
    species = "Unknown"

    def __init__(self, name, age):
        self.name = name        # instance variable
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound."

    def __str__(self):
        return f"Animal({self.name}, {self.age})"


class Dog(Animal):              # Inheritance
    def speak(self):            # Method overriding
        return f"{self.name} says Woof!"

    def fetch(self):
        return f"{self.name} fetches the ball!"


dog = Dog("Buddy", 3)
print(dog.speak())              # Buddy says Woof!
print(dog.fetch())
print(isinstance(dog, Animal))  # True


# ------------------------------------------------------------
# 17. MODULES & IMPORTS
# ------------------------------------------------------------
import math
import random
import datetime

print(math.sqrt(16))            # 4.0
print(math.pi)                  # 3.14159...
print(random.randint(1, 10))    # random int
print(datetime.date.today())    # today's date

from math import factorial
print(factorial(5))             # 120


# ------------------------------------------------------------
# 18. LIST / DICT / SET COMPREHENSIONS
# ------------------------------------------------------------
# List comprehension with condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# Dict comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict)

# Set comprehension
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}
print(unique_squares)


# ------------------------------------------------------------
# 19. USEFUL BUILT-IN FUNCTIONS
# ------------------------------------------------------------
nums = [3, 1, 4, 1, 5, 9, 2, 6]

print(min(nums))        # 1
print(max(nums))        # 9
print(sum(nums))        # 31
print(sorted(nums))     # sorted list
print(list(reversed(nums)))
print(list(enumerate(["a", "b", "c"])))  # [(0,'a'), (1,'b'), (2,'c')]
print(list(zip([1,2,3], ["a","b","c"]))) # [(1,'a'), (2,'b'), (3,'c')]
print(list(map(lambda x: x*2, nums)))    # double each
print(list(filter(lambda x: x>3, nums)))# filter > 3


# ------------------------------------------------------------
# 20. STRING FORMATTING
# ------------------------------------------------------------
name, score = "Alice", 95.5

# f-string (recommended)
print(f"{name} scored {score:.2f}%")

# .format()
print("{} scored {:.2f}%".format(name, score))

# % formatting (old style)
print("%s scored %.2f%%" % (name, score))