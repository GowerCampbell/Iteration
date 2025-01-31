# test.py
# A collection of experiments and code snippets for testing Python concepts.

# ====================
# Experiment 1: Basic For Loop
# ====================
print("\nExperiment 1: Basic For Loop")
for i in range(5):
    print(f"Current value of i: {i}")

# ====================
# Experiment 2: While Loop with User Input
# ====================
print("\nExperiment 2: While Loop with User Input")
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Enter a word (or type 'exit' to stop): ")
    print(f"You entered: {user_input}")

# ====================
# Experiment 3: List Comprehension
# ====================
print("\nExperiment 3: List Comprehension")
squares = [x**2 for x in range(10)]
print(f"Squares of numbers 0-9: {squares}")

# ====================
# Experiment 4: Nested Loops
# ====================
print("\nExperiment 4: Nested Loops")
for i in range(3):
    for j in range(3):
        print(f"i = {i}, j = {j}")

# ====================
# Experiment 5: String Manipulation
# ====================
print("\nExperiment 5: String Manipulation")
text = "Hello, Python!"
print(f"Original text: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Reversed: {text[::-1]}")

# ====================
# Experiment 6: Dictionary Iteration
# ====================
print("\nExperiment 6: Dictionary Iteration")
student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
for name, grade in student_grades.items():
    print(f"{name} scored {grade}")

# ====================
# Experiment 7: Error Handling
# ====================
print("\nExperiment 7: Error Handling")
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Invalid input! Please enter a valid number.")

# ====================
# Experiment 8: Infinite Loop with Break
# ====================
print("\nExperiment 8: Infinite Loop with Break")
counter = 0
while True:
    print(f"Counter: {counter}")
    counter += 1
    if counter >= 5:
        break

# ====================
# Experiment 9: Using Enumerate
# ====================
print("\nExperiment 9: Using Enumerate")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# ====================
# Experiment 10: Random Number Generation
# ====================
print("\nExperiment 10: Random Number Generation")
import random
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

# ====================
# Experiment 11: File Handling
# ====================
print("\nExperiment 11: File Handling")
with open("test_file.txt", "w") as file:
    file.write("This is a test file.\nPython is awesome!")

with open("test_file.txt", "r") as file:
    content = file.read()
    print("\nFile Content:")
    print(content)

# ====================
# Experiment 12: Function with Default Arguments
# ====================
print("\nExperiment 12: Function with Default Arguments")
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")
greet()

# ====================
# Experiment 13: Lambda Functions
# ====================
print("\nExperiment 13: Lambda Functions")
multiply = lambda x, y: x * y
print(f"Result of multiplying 3 and 4: {multiply(3, 4)}")

# ====================
# Experiment 14: Filter and Map
# ====================
print("\nExperiment 14: Filter and Map")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Even numbers: {even_numbers}")
print(f"Squared numbers: {squared_numbers}")

# ====================
# Experiment 15: Using Zip
# ====================
print("\nExperiment 15: Using Zip")
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# ====================
# Experiment 16: Set Operations
# ====================
print("\nExperiment 16: Set Operations")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference: {set1.difference(set2)}")

# ====================
# Experiment 17: Generator Expressions
# ====================
print("\nExperiment 17: Generator Expressions")
squares_gen = (x**2 for x in range(10))
print("Squares using generator expression:")
for square in squares_gen:
    print(square, end=" ")
print()

# ====================
# Experiment 18: Using `any` and `all`
# ====================
print("\nExperiment 18: Using `any` and `all`")
numbers = [1, 2, 3, 4, 5]
print(f"Any number greater than 3? {any(x > 3 for x in numbers)}")
print(f"All numbers greater than 3? {all(x > 3 for x in numbers)}")

# ====================
# Experiment 19: Working with Dates
# ====================
print("\nExperiment 19: Working with Dates")
from datetime import datetime
now = datetime.now()
print(f"Current date and time: {now}")
print(f"Formatted date: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# ====================
# Experiment 20: Using `collections.Counter`
# ====================
print("\nExperiment 20: Using `collections.Counter`")
from collections import Counter
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(f"Word count: {word_count}")

# ====================
# End of Experiments
# ====================
print("\nAll experiments completed!")
