
# **Python Iteration**

This repository demonstrates the concept of **iteration** in Python using `for` loops, `while` loops, and nested loops. Iteration is the process of repeatedly executing a block of code, which is essential for tasks like processing data, creating patterns, or performing calculations.

The repository includes practical examples to help you understand how iteration works and how to apply it in real-world scenarios.

---

## **Table of Contents**
1. [What is Iteration?](#what-is-iteration)
2. [Key Examples](#key-examples)
   - [For Loops](#for-loops)
   - [While Loops](#while-loops)
   - [Nested Loops](#nested-loops)
3. [Files in the Repository](#files-in-the-repository)
4. [How to Use](#how-to-use)
5. [Class Notes](#class-notes)
6. [Conclusion](#conclusion)

---

## **What is Iteration?** <a name="what-is-iteration"></a>

Iteration refers to the process of repeatedly executing a set of instructions or code. It is useful when you need to perform an operation multiple times, such as printing numbers, performing calculations, or creating patterns. In Python, there are primarily two types of iteration:

1. **`for` loops**: Used when you know the number of iterations beforehand (e.g., iterating over a range of numbers or a list).
2. **`while` loops**: Used when the number of iterations depends on a condition (e.g., user input or a calculation).

---

## **Key Examples** <a name="key-examples"></a>

### **1. `for` Loops** <a name="for-loops"></a>
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

### **2. `while` Loops** <a name="while-loops"></a>
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

### **3. Nested Loops** <a name="nested-loops"></a>
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

## **BootCamp Files in the Repository** <a name="files-in-the-repository"></a>

1. **[`pattern.py`](CoGrammar-BootCamp-Tasks/pattern.py)**: Demonstrates nested loops to create patterns and multiplication tables.
2. **[`while.py`](CoGrammar-BootCamp-Tasks/while.py)**: Implements `while` loops for dynamic number input, summing, and averaging.
3. **[`test.py`](CoGrammar-BootCamp-Tasks/test.py)**: Contains additional test code and experiments.

---

## **How to Use** <a name="how-to-use"></a>

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bootcamp-iteration-tasks.git
   ```
2. Navigate to the repository directory:
   ```bash
   cd bootcamp-iteration-tasks
   ```
3. Run the Python scripts:
   ```bash
   python pattern.py
   python while.py
   python test.py
   ```

---

## **Class Notes** <a name="class-notes"></a>

For detailed explanations and additional examples, refer to the **[Class Notes](CoGrammar-BootCamp-Tasks/knotes.md)**.

---

## **Conclusion** <a name="conclusion"></a>

This repository will provide my practical examples of iteration I've used in Python, offering an opportunity for me to explore different loop structures and understand their use in real-world scenarios. Starting as a beginner like me or looking to refresh your knowledge, these examples will help myself master the concept of iteration.

Feel free to explore the code, modify it, and experiment with your own examples! If you have any questions or suggestions for me, please open an issue or submit a pull request. Happy coding! 🚀

---

### **Quick Links**
- [What is Iteration?](#what-is-iteration)
- [For Loops](#for-loops)
- [While Loops](#while-loops)
- [Nested Loops](#nested-loops)
- [Files in the Repository](#files-in-the-repository)
- [How to Use](#how-to-use)
- [Class Notes](#class-notes)
- [Conclusion](#conclusion)

