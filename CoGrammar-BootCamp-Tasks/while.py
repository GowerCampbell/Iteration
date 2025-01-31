# While Iteration Task 1 - Written by Gower Campbekk
# Objective: Demonstrate my understanding of while loops and their application
# in repetitive tasks by working with user input. To enhance my problem-solving
# and understanding of loops and conditional logic.

# ====================
# Program Description:
# ====================
# This program continually asks the user to enter a number.
# When the user enters "-1", the program stops.
# The program calculates the average of all valid numbers entered, excluding -1.
# Note: 0 is not a valid input.

# ====================
# Variables:
# ====================
total = 0  # To collect the sum of valid numbers
count = 0  # To count the number of valid inputs

# ====================
# Main Program Loop:
# ====================
print("\nThis is a continuous loop asking you to enter integers.")
print("Enter -1 to stop the loop. Remember, 0 is not a valid number.\n")

# Initialize a flag to control the loop
running = True

while running:
    try:
        # Prompt the user for input
        user_input = int(input("Enter an integer: "))

        # Check if the user wants to stop the loop
        if user_input == -1:
            running = False  # Exit the loop if the user enters -1
        # Check if the input is 0 (invalid)
        elif user_input == 0:
            print("\n0 is not a valid number. Please try again.")
        else:
            # If the input is valid, update the total and count
            total += user_input
            count += 1

    except ValueError:
        # Handle non-integer inputs
        print("\nInvalid input. Please enter an integer.")

# ====================
# Calculate and Display the Average:
# ====================
if count > 0:
    average = total / count
    print(f"\nThe average of the valid numbers is: {average:.2f}")
else:
    print("\nNo valid numbers were entered.")

# ====================
# Summary:
# ====================
# This program uses a 'while' loop to repeatedly perform actions based on user input:
# 1. Continuously prompts the user to enter numbers.
# 2. Stops the loop when the user enters -1.
# 3. Calculates the average of the numbers entered, excluding -1.
# 4. Handles invalid inputs (0 and non-integer values) gracefully.
