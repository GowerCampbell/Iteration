# While Loops in Python

This document explains how to use `while` loops in Python. It covers the basic syntax, common use cases, and practical examples to help you understand how to implement and control loops in your programs.

---

## Key Concepts

### 1. **What is a While Loop?**
A `while` loop repeatedly executes a block of code as long as a specified condition is `True`. It is useful when you don’t know in advance how many times the loop needs to run.

#### Syntax
```python
while condition:
    # Code to execute while the condition is True
```

---

### 2. **Basic Example**
The following example demonstrates a simple `while` loop that counts from 1 to 5.

```python
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment count by 1
```

#### Output:
```
1
2
3
4
5
```

---

### 3. **Common Use Cases**

#### **a. User Input Validation**
Use a `while` loop to repeatedly ask the user for input until they provide a valid response.

```python
while True:
    try:
        number = int(input("Enter a number: "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a number.")
```

#### **b. Infinite Loops**
An infinite loop runs forever unless explicitly stopped. Use `break` to exit the loop when a condition is met.

```python
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input.lower() == "exit":
        break
    print("You typed:", user_input)
```

#### **c. Counting Down**
Use a `while` loop to count down from a specified number.

```python
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1  # Decrement countdown by 1
print("Blast off!")
```

#### Output:
```
5
4
3
2
1
Blast off!
```

---

### 4. **Controlling Loops**

#### **a. `break` Statement**
The `break` statement exits the loop immediately, even if the condition is still `True`.

```python
while True:
    user_input = input("Type 'quit' to exit: ")
    if user_input.lower() == "quit":
        break
    print("You typed:", user_input)
```

#### **b. `continue` Statement**
The `continue` statement skips the rest of the loop's code and goes back to the condition check.

```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the rest of the loop for count = 3
    print(count)
```

#### Output:
```
1
2
4
5
```

#### **c. `else` Clause**
The `else` clause executes after the loop finishes, but only if the loop ends normally (not via `break`).

```python
count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("Loop finished!")
```

#### Output:
```
1
2
3
Loop finished!
```

---

### 5. **Practical Examples**

#### **a. Password Validation**
Ask the user to enter a password until they provide the correct one.

```python
password = "python123"
while True:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")
```

#### **b. Number Guessing Game**
Create a simple number guessing game using a `while` loop.

```python
import random

number = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations! You guessed correctly.")
        break
    else:
        print("Try again!")
```

#### **c. Summing Numbers**
Ask the user to enter numbers and calculate their sum until they enter `0`.

```python
total = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total += number
print(f"The total is: {total}")
```

---

## Conclusion
`while` loops are a powerful tool in Python for repeating a block of code as long as a condition is `True`. They are particularly useful for tasks like user input validation, counting, and creating interactive programs. By mastering `while` loops, I can write more dynamic and efficient code.

---

### Additional Resources
- [Python Documentation: While Loops](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
- [Real Python: Python While Loops](https://realpython.com/python-while-loop/)

