# Nested Loops in Python

This document explains how to use **nested loops** in Python. Nested loops are loops inside other loops, and they are useful for working with multi-dimensional data, such as matrices, grids, or nested lists.

---

## Key Concepts

### 1. **What are Nested Loops?**
A nested loop is a loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop. Nested loops are commonly used for:
- Iterating through multi-dimensional data structures.
- Generating patterns or grids.
- Performing repetitive tasks with multiple levels of iteration.

#### Syntax
```python
for outer_item in outer_sequence:
    for inner_item in inner_sequence:
        # Code to execute
```

---

### 2. **Basic Example**
The following example demonstrates a simple nested loop that prints a multiplication table.

```python
for i in range(1, 6):  # Outer loop
    for j in range(1, 6):  # Inner loop
        print(f"{i} * {j} = {i * j}")
    print()  # Add a blank line after each row
```

#### Output:
```
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10

...
```

---

### 3. **Common Use Cases**

#### **a. Generating Patterns**
Nested loops are often used to generate patterns, such as stars or numbers.

```python
# Print a right-angled triangle
for i in range(1, 6):  # Outer loop for rows
    for j in range(i):  # Inner loop for columns
        print("*", end=" ")
    print()  # Move to the next line
```

#### Output:
```
* 
* * 
* * * 
* * * * 
* * * * * 
```

#### **b. Iterating Through a 2D List**
Nested loops are useful for working with 2D lists (lists of lists).

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:  # Outer loop for rows
    for item in row:  # Inner loop for items in each row
        print(item, end=" ")
    print()  # Move to the next line
```

#### Output:
```
1 2 3 
4 5 6 
7 8 9 
```

#### **c. Creating a Grid**
Nested loops can be used to create grids or tables.

```python
for i in range(3):  # Outer loop for rows
    for j in range(3):  # Inner loop for columns
        print(f"({i}, {j})", end=" ")
    print()  # Move to the next line
```

#### Output:
```
(0, 0) (0, 1) (0, 2) 
(1, 0) (1, 1) (1, 2) 
(2, 0) (2, 1) (2, 2) 
```

---

### 4. **Controlling Nested Loops**

#### **a. `break` Statement**
The `break` statement exits the **innermost loop** immediately.

```python
for i in range(3):  # Outer loop
    for j in range(3):  # Inner loop
        if j == 1:
            break  # Exit the inner loop when j = 1
        print(f"({i}, {j})")
```

#### Output:
```
(0, 0)
(1, 0)
(2, 0)
```

#### **b. `continue` Statement**
The `continue` statement skips the rest of the **current iteration** of the innermost loop.

```python
for i in range(3):  # Outer loop
    for j in range(3):  # Inner loop
        if j == 1:
            continue  # Skip when j = 1
        print(f"({i}, {j})")
```

#### Output:
```
(0, 0)
(0, 2)
(1, 0)
(1, 2)
(2, 0)
(2, 2)
```

---

### 5. **Practical Examples**

#### **a. Finding Common Elements**
Use nested loops to find common elements between two lists.

```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common_elements = []
for item1 in list1:  # Outer loop
    for item2 in list2:  # Inner loop
        if item1 == item2:
            common_elements.append(item1)

print("Common elements:", common_elements)
```

#### Output:
```
Common elements: [3, 4]
```

#### **b. Generating a Chessboard**
Use nested loops to simulate a chessboard.

```python
for row in range(8):  # Outer loop for rows
    for col in range(8):  # Inner loop for columns
        if (row + col) % 2 == 0:
            print("W", end=" ")  # White square
        else:
            print("B", end=" ")  # Black square
    print()  # Move to the next line
```

#### Output:
```
W B W B W B W B 
B W B W B W B W 
W B W B W B W B 
B W B W B W B W 
W B W B W B W B 
B W B W B W B W 
W B W B W B W B 
B W B W B W B W 
```

#### **c. Calculating Matrix Multiplication**
Use nested loops to multiply two matrices.

```python
matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [5, 6],
    [7, 8]
]

result = [
    [0, 0],
    [0, 0]
]

for i in range(len(matrix1)):  # Outer loop for rows of matrix1
    for j in range(len(matrix2[0])):  # Inner loop for columns of matrix2
        for k in range(len(matrix2)):  # Inner loop for rows of matrix2
            result[i][j] += matrix1[i][k] * matrix2[k][j]

print("Result of matrix multiplication:")
for row in result:
    print(row)
```

#### Output:
```
Result of matrix multiplication:
[19, 22]
[43, 50]
```

---

## Conclusion
Nested loops are a powerful tool in Python for working with multi-dimensional data, generating patterns, and solving complex problems. By mastering nested loops, I can write more efficient and versatile programs.

---

### Additional Resources
- [Python Documentation: Loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Real Python: Nested Loops](https://realpython.com/python-for-loop/)

