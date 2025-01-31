# Python Iteration

This repository demonstrates the concept of **iteration** in Python using **for loops**, **while loops**, and **nested loops**. Iteration is the process of repeatedly executing a block of code, which is essential for tasks like processing data, creating patterns, or performing calculations.

The repository includes **practical examples** to help you understand how iteration works and how to apply it in real-world scenarios.

---

## Table of Contents
1. [What is Iteration?](#what-is-iteration)
2. [Key Examples](#key-examples)
   - [For Loops](#for-loops)
   - [While Loops](#while-loops)
   - [Nested Loops](#nested-loops)
3. [Practical Applications](#practical-applications)
4. [Files in the Repository](#files-in-the-repository)
5. [How to Use](#how-to-use)
6. [Class Notes](#class-notes)
7. [Conclusion](#conclusion)

---

## What is Iteration?
Iteration refers to the process of repeatedly executing a set of instructions or code. It is useful when you need to perform an operation multiple times, such as printing numbers, performing calculations, or creating patterns. In Python, there are primarily two types of iteration:

- **`for` loops**: Used when you know the number of iterations beforehand (e.g., iterating over a range of numbers or a list).
- **`while` loops**: Used when the number of iterations depends on a condition (e.g., user input or a calculation).

---

## Key Examples

### 1. **For Loops**
#### Example: Printing Even Numbers
This example prints all even numbers between 1 and 999 using a `for` loop:

```python
for num in range(1, 1000):
    if num % 2 == 0:
        print(num)
```

- The loop iterates through each number in the range from 1 to 999.
- It checks if the number is even (i.e., the remainder when divided by 2 is 0).
- If true, it prints the number.

#### Example: Multiplication Table
This example generates a multiplication table using nested `for` loops:

```python
for x in range(1, 6):
    for y in range(1, 6):
        print("{} * {} = {}".format(x, y, x * y))
```

- The outer loop controls the rows.
- The inner loop handles the columns.
- The result of multiplying the row number (`x`) by the column number (`y`) is printed.

---

### 2. **While Loops**
#### Example: Input Validation
This example uses a `while` loop to repeatedly ask the user for input until a valid number is entered:

```python
number = int(input("Enter a number less than 100: "))
while number > 100:
    print("Please try again")
    number = int(input("Enter a number less than 100: "))
```

- The loop continues until the user enters a number less than or equal to 100.

#### Example: Infinite Loop
This example demonstrates an infinite loop that prints "I can see infinity":

```python
i = 10
while i < 14:
    print("I can see infinity")
```

- The condition (`i < 14`) is always true, so the loop runs indefinitely until manually stopped.

#### Example: Sum of Even Numbers
This example sums even numbers until the total exceeds 250:

```python
sum1 = 0
i = 0
while sum1 <= 250:
    sum1 += i
    i += 2
    print(sum1)
```

- The loop adds even numbers (`i`) to the total (`sum1`).
- It stops when the total exceeds 250.

---

### 3. **Nested Loops**
#### Example: Star Patterns
This example creates star patterns based on user input:

```python
given_number = int(input("Enter a number: \n"))

if given_number % 2 == 0:  # If the number is even
    stars = "*"
    for i in range(0, 10):
        print(stars)
        stars = stars + "*"
else:  # If the number is odd
    stars = "**********"
    for i in range(0, 10):
        index = 10 - i
        print(stars[0:index])  # Print fewer stars as the loop progresses
```

- If the number is even, it prints an increasing star pattern.
- If the number is odd, it prints a decreasing star pattern.

---

## Practical Applications

### 1. **User Input Validation**
Use `while` loops to repeatedly ask the user for input until they provide valid data.

```python
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative. Try again.")
        else:
            break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a number.")
```

### 2. **Password Authentication**
Use `while` loops and conditionals to implement secure login systems.

```python
password = "secure123"
attempts = 3

while attempts > 0:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts remaining.")

if attempts == 0:
    print("Access denied. Please try again later.")
```

### 3. **Data Filtering**
Use `for` loops and conditionals to filter data from a list.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)
```

### 4. **Generating Reports**
Use loops and conditionals to process and format data for reports.

```python
sales = [
    {"product": "Apple", "quantity": 10, "price": 1.50},
    {"product": "Banana", "quantity": 5, "price": 0.75},
    {"product": "Orange", "quantity": 8, "price": 1.25}
]

total_sales = 0
print("Sales Report:")
print("-------------")
for item in sales:
    total = item["quantity"] * item["price"]
    total_sales += total
    print(f"{item['product']}: {item['quantity']} units, Total: ${total:.2f}")
print("-------------")
print(f"Total Sales: ${total_sales:.2f}")
```

---

## Files in the Repository
Here are the key files in this repository:

- **[`For-Loops.md`](For-Loops.md)**: Detailed explanation and examples of `for` loops.
- **[`While-Loops.md`](While-Loops.md)**: Detailed explanation and examples of `while` loops.
- **[`Nested-Loops.md`](Nested-Loops.md)**: Detailed explanation and examples of nested loops.
- **[`Practical-Applications.md`](Practical-Applications.md)**: Real-world examples of loops and conditionals.
- **[`pattern.py`](CoGrammar-BootCamp-Tasks/pattern.py)**: Demonstrates nested loops to create patterns and multiplication tables.
- **[`while.py`](CoGrammar-BootCamp-Tasks/while.py)**: Implements `while` loops for dynamic number input, summing, and averaging.
- **[`test.py`](CoGrammar-BootCamp-Tasks/test.py)**: Contains additional test code and experiments.

---

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. Navigate to the repository:
   ```bash
   cd your-repo-name
   ```
3. Run the Python files to see the examples in action:
   ```bash
   python pattern.py
   python while.py
   ```

---

## Class Notes
For detailed explanations and additional examples, refer to the [Class Notes](CoGrammar-BootCamp-Tasks/knotes.py).

---

## Conclusion
This repository provides **practical examples** of iteration in Python, offering an opportunity to explore different loop structures and understand their use in real-world scenarios. Whether you're a beginner or looking to refresh your knowledge, these examples will help you master the concept of iteration.

Feel free to explore the code, modify it, and experiment with your own examples! If you have any questions or suggestions, please open an issue or submit a pull request. Happy coding! 🚀

---

### Quick Links
- [What is Iteration?](#what-is-iteration)
- [For Loops](#for-loops)
- [While Loops](#while-loops)
- [Nested Loops](#nested-loops)
- [Practical Applications](#practical-applications)
- [Files in the Repository](#files-in-the-repository)
- [How to Use](#how-to-use)
- [Class Notes](#class-notes)
- [Conclusion](#conclusion)


