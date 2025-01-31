# **For Loops in Python: Additional Examples**

`for` loops are a powerful tool in Python for iterating over sequences like lists, tuples, strings, and ranges. Below are some practical examples to help you understand and master `for` loops.

---

## **1. Basic For Loop**
The simplest use of a `for` loop is to iterate over a range of numbers.

```python
# Print numbers from 0 to 4
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

---

## **2. Iterating Over a List**
You can use a `for` loop to iterate over elements in a list.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

---

## **3. Using `enumerate` to Get Index and Value**
The `enumerate` function allows you to loop over a list while keeping track of the index.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

**Output:**
```
Index 0: apple
Index 1: banana
Index 2: cherry
```

---

## **4. Nested For Loops**
You can nest `for` loops to iterate over multiple sequences or create patterns.

```python
# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} * {j} = {i * j}")
    print("")  # Add a blank line after each row
```

**Output:**
```
1 * 1 = 1
1 * 2 = 2
...
5 * 5 = 25
```

---

## **5. Iterating Over a String**
You can loop through each character in a string.

```python
text = "Python"
for char in text:
    print(char)
```

**Output:**
```
P
y
t
h
o
n
```

---

## **6. Using `zip` to Iterate Over Multiple Lists**
The `zip` function allows you to iterate over multiple lists simultaneously.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
```

**Output:**
```
Alice scored 85
Bob scored 90
Charlie scored 78
```

---

## **7. Looping Over a Dictionary**
You can iterate over the keys, values, or key-value pairs in a dictionary.

```python
student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

# Iterate over keys
for name in student_grades:
    print(name)

# Iterate over values
for grade in student_grades.values():
    print(grade)

# Iterate over key-value pairs
for name, grade in student_grades.items():
    print(f"{name}: {grade}")
```

**Output:**
```
Alice
Bob
Charlie
85
90
78
Alice: 85
Bob: 90
Charlie: 78
```

---

## **8. Using `range` with a Step**
You can specify a step value in the `range` function to skip numbers.

```python
# Print even numbers between 0 and 10
for i in range(0, 11, 2):
    print(i)
```

**Output:**
```
0
2
4
6
8
10
```

---

## **9. Looping Over a List with `break` and `continue`**
You can use `break` to exit a loop early and `continue` to skip the current iteration.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num == 5:
        break  # Exit the loop when num is 5
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
```

**Output:**
```
1
3
```

---

## **10. List Comprehensions**
List comprehensions provide a concise way to create lists using `for` loops.

```python
# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)
```

**Output:**
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

## **11. Looping Over Files**
You can use a `for` loop to read lines from a file.

```python
# Example: Reading a file line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Remove extra newline characters
```

---

## **12. Using `else` with For Loops**
The `else` block in a `for` loop executes after the loop completes normally (i.e., without a `break`).

```python
for i in range(3):
    print(i)
else:
    print("Loop completed!")
```

**Output:**
```
0
1
2
Loop completed!
```

---

## **13. Looping Over a Set**
You can iterate over elements in a set.

```python
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
```

**Output:**
```
red
green
blue
```

---

## **14. Looping Over a Tuple**
Tuples can also be iterated over using a `for` loop.

```python
coordinates = (10, 20, 30)
for value in coordinates:
    print(value)
```

**Output:**
```
10
20
30
```

---

## **15. Using `reversed` to Loop Backwards**
You can use the `reversed` function to iterate over a sequence in reverse order.

```python
numbers = [1, 2, 3, 4, 5]
for num in reversed(numbers):
    print(num)
```

**Output:**
```
5
4
3
2
1
```

---

## **16. Looping Over a Generator**
Generators allow you to iterate over large datasets without storing them in memory.

```python
# Generator expression
squares = (x**2 for x in range(5))
for square in squares:
    print(square)
```

**Output:**
```
0
1
4
9
16
```

---

## **17. Looping Over a 2D List**
You can use nested loops to iterate over a 2D list (list of lists).

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # Move to the next line after each row
```

**Output:**
```
1 2 3 
4 5 6 
7 8 9 
```

---

## **18. Using `itertools` for Advanced Iteration**
The `itertools` module provides powerful tools for advanced iteration.

```python
import itertools

# Infinite loop with itertools.count
for i in itertools.count(start=1, step=2):
    if i > 10:
        break
    print(i)
```

**Output:**
```
1
3
5
7
9
```

---

## **Conclusion**
`for` loops are incredibly versatile and can be used in a wide variety of scenarios. Whether yI'm working with lists, dictionaries, files, or even custom objects, mastering `for` loops is essential for me to start writing efficient and readable Python code.

Feel free to experiment with these examples and adapt them to my own projects! 🚀

