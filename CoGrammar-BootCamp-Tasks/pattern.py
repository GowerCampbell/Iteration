# Pattern Iteration Written by Gower Campbell

# Objective: To demonstrate my knowlege of for loops and conditional logic 
# by generating a specfic pattern output:

# *********** First Example ***********
# loop = int(input('Please provide the range of stars: '))

# Defining a for loop that iterates forward 
# through a sequence of numbers, starting at 1 and 
# stopping just before loop + 1

# for iteration in range(1, loop + 1):
 # print('*' * iteration)

# This generates a sequence in reverse order, 
# starting from loop - 1 and ending just before 0.

# for iteration in range(loop - 1, 0, -1): 
#  print("*" * iteration)

# *********** Second Example ***********

# Using a if-elif statement in combination with a single for loop;

range_of_stars = int(input("Enter the number of stars for the range: "))

for i in range(1, 2 * range_of_stars):

   # Using the iteration = 1, 2, 3, ... from the users input.
   # To create a continuous sequence of numbers using the range(start, stop/input).

    if i <= range_of_stars:

        # Applys the value on the left (i) is either less than or equal to 
        # the value on the right (range_of_stars) then it becomes True, 
        # running the code below.

        print("*" * range_of_stars) 
        # Prints the '*' by the range_of_stars (increasing the pattern) 
        # till the input/number is reached becoming false.
        # because the '2 * range_of_stars' is doubling my range,
        # It moves onto the next part;

    elif i > range_of_stars: 
        # If the 'i'teration is greater than the range_of_stars
        # This then handles the next step by:

        print("*" * (2 * range_of_stars - i))
        # It prints out the logic that once the range of stars is met
        # The code starts to subtract the 'i' from '2 * range_of_stars'
        # Acting as the variable that counters the value of range_of_stars?

# ************ ***********

# Dynamically create and ouput lines of varying patterns (e.g. **,*, *****)
# Apply logic within the loop to control the pattern baed on conditions
# Input the conditions and then set off the conditions of if-elif to create pattern.


