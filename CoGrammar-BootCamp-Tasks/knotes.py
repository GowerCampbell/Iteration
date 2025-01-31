
# Iteration Knotes Written By Gower Campbell
# Refers to the process of executing a set of instructions repeatedly.
# 'For' loops and 'while' loops are used to handle repetitive tasks.
# Condition-based iteration allows the loop to continue or stop
# based on a condition, either for a predetermined number of times or until a condition is met.

# For loops are control flow structures used to iterate over a sequence:
# (List, tuple, string, etc.) and execute a block of code.

# Knote: George Boole (1815-1864) introduced the Boolean data type.

# Define a list of fruits
fruits = ["apple", "banana", "cherry", "date"]

# For loop to iterate over the list of fruits
for fruit in fruits:
    print(fruit)
# Result: apple, banana, cherry, date

# A 'while' loop is a general form of loop statement.
# It takes a code block and keeps executing it while a given condition stays TRUE.
# The loop stops when the condition becomes FALSE.

# Syntax:
# while condition:
#     indented statements

# Example 1:
# Check if the count is less than 5. If this condition is True,
# the code block will execute until the condition is False, and the loop will terminate.
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# Example 2:
# An update statement that shows a 'while' loop
sum1 = 0
i = 2
while sum1 <= 250:
    sum1 += i
    i += 2
    print(sum1)

# Sums successive even integers 2 + 4 + 6 + 8 until the total is greater than 250.

# This is an event-controlled loop (as opposed to counter-controlled loops like 'for' loops).

# The range() function generates a sequence of numbers based on the arguments you provide:
# range(start, stop, step)
# Start: The starting value of the sequence (inclusive). If not specified, it defaults to 0.
# Stop: The ending value of the sequence (exclusive). This is a required argument.
# Step: The increment between each value in the sequence. If not specified, it defaults to 1.

# Example: Using range() in a for loop
for i in range(1, 6):  # This will iterate from 1 to 5
    print(i)
# Output: 1, 2, 3, 4, 5

# Complete repetitive tasks efficiently:
for i in range(1, 11):
    print(i)
# Output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Advantages of loops:
# Efficiency: Reduces repetitive code.
# Flexibility: Can handle dynamic data.
# Scalability: Works with large datasets.
# Maintenance: Easier to update and debug.

# While loop example:
i = 0
while i < 10:
    i += 1  # Shorthand for i = i + 1
    print(i)

# The assignment statement used to update the variable i in line three: i += 1.
# This adds 1 to the variable i in each iteration until i == 10.
# At this point, the logical test will fail because i is no longer less than 10 but equal to 10 (i < 10).

# Declare a counter/control variable. The code above uses i = 0.
# This creates a variable called i that contains the value 0.

# Increase the counter/control variable in the loop. In the loop above, this is done with the instruction i += 1,
# which increases i by 1.

# Specify a condition to control when the loop ends. The condition of the while loop above is i < 10.

# For loops don't explicitly declare a counter or specify a condition.

# Infinite Loops
# A loop that runs forever if the condition never becomes False.
# Example: Using a while loop with boolean data types
keep_running = True

while keep_running:
    print("The loop is running.")
    keep_running = False  # Set to False to exit the loop
print("The loop has ended.")

# The while loop continues to execute as long as keep_running is True.
# keep_running is set to False to ensure the loop exits after the first iteration.

# Terminating Infinite Loops
# To avoid freezing your IDE or terminal:
# Identify an infinite loop and press Ctrl+C to interrupt the running program and stop it effectively.

# Break Statements
# Used to exit the loop, even if the condition of the loop hasn't been met.
# Example:
my_number = 0
while my_number < 100:
    my_number += 1
    if my_number == 23:
        break
    print(my_number)

# The loop breaks when it reaches 23 and stops.

# Continue Statements
# Used to skip the rest of the current iteration and move to the next iteration.
# Example:
my_number = 0
while my_number < 100:
    my_number += 1
    if my_number == 23:
        continue
    print(my_number)

# The loop skips printing the number 23 but continues to 100.

# What is a For Loop?
# A counter-controlled loop that begins with a start value and counts up to an end value.

# Syntax:
for index_variable in sequence:
    statements

# 'For' holds each of the values of the sequence as we move through it.
# The index variable can tell you what iteration the loop is on.

# In each iteration (or repetition) of the for loop, the code that is indented is repeated.
# Remember when using the range() function:
# The start index is included, and the end index is not included.

# Example:
for i in range(1, 10):
    print(i)
# Output: 1, 2, 3, 4, 5, 6, 7, 8, 9

# You can use an if statement within a for loop:
for i in range(1, 10):
    if i > 5:
        print(i)

# Initialize loop: The loop needs a variable as its counter variable.
# Loop Test: The loop test is a Boolean expression in Python that evaluates to either True or False.
# The loop test expression is evaluated before any iteration. If the condition is True,
# the program control is passed to the loop body; if False, control passes to the first statement after the loop.
# Update Statement: Assigning new values to the loop control variables with an increment (e.g., i += 1).
# This is always executed after the loop body, and control passes to the loop test to mark the beginning of the next iteration.

# Loops can also include a break statement to immediately exit the loop.

# Example: Searching for a number in a list
num_list = [1, 2, 3, 4, 5]

# Initialize a flag to indicate if the number is found
found = False

# Prompt the user to input a number from 1 to 10
num = int(input("Input a number from 1 to 10 and find out if it's in our list: "))

# Check if the input number is within the valid range
if num < 1 or num > 10:
    # Inform the user if the number is out of range
    print("Number out of range")
else:
    # Iterate through the list to check if the number is present
    for number in num_list:
        if num == number:
            # Set the flag to True if the number is found and exit the loop
            found = True
            break
    # Print the result indicating whether the number is in the list or not
    print(f"List contains {num}: {found}")

# Important application of the break statement:
# The number of iterations depends on the amount of data in the file.

# In selecting a loop construct (while loop or for loop), consider the nature of the task.

# Nested Loop Codes
# A loop within a loop. Each time the outer loop is executed, the inner loop is executed right from the start.
# Knote: All the iterations of the inner loop are executed with each iteration of the outer loop.

# Syntax for a nested 'for' loop in another 'for' loop:
for iterating_var_1 in sequence:
    for iterating_var_2 in sequence:
        statements(s)
    statements(s)

# Syntax for a nested 'while' loop in another 'while' loop:
while condition_1:
    while condition_2:
        statement(s)
    statements(s)

# Syntax for a 'while' loop in a 'for' loop:
for iterating_var in sequence:
    while condition:
        statement(s)
    statements(s)

# Example: Nested Loop
for x in range(1, 6):
    for y in range(1, 6):
        print(f"{x} * {y} = {x*y}")
    print(" ")

# Remember the iteration: there needs to be a space between the statements.

# Trace Tables
# Used for data checking to ensure the logic of the code makes sense.
# Create a table where all the values of the variables are tracked for each iteration.

# Nature of nested loops: The inner loop iterates five times before the outer loop.
# The x will remain the same value while y loops through all its iterations.
# y cycles from one to five for the same value of x.

# All your code to choose different paths:
# Conditional operators: if, elif, and else
# Comparison Operators: ==, +=, -=, >=, <=, !=
# Logical operators: and, or, in
