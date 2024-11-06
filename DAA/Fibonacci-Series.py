# Fibonacci Program with Step Counting and Explanations

# Function to calculate Fibonacci numbers and count steps
def fibonacci(n):
    # Initialize first two Fibonacci numbers
    a, b = 0, 1
    # Step counter initialized to 0
    step_count = 0

    # Loop through the range to find Fibonacci up to n
    for i in range(n):
        # Increment step count in each loop iteration
        step_count += 1
        # Swap values: a gets value of b, b gets sum of a and b
        a, b = b, a + b

    # Return nth Fibonacci number and step count
    return a, step_count


# User input for Fibonacci number position
n = int(input("Enter the position of the Fibonacci number you want: "))

# Calculate Fibonacci number and steps taken
fib_num, steps = fibonacci(n)

# Display the result
print(f"The {n}th Fibonacci number is: {fib_num}")
print(f"Total steps taken to compute: {steps}")

# Explanation:
# - The program defines a function `fibonacci` that takes a number `n` as input.
# - This function calculates the nth Fibonacci number using an iterative approach.
# - Inside the function:
#   - Variables `a` and `b` store the two preceding Fibonacci numbers.
#   - The `step_count` variable tracks the number of iterations (steps) taken.
#   - For each iteration, we compute the next Fibonacci number by adding the previous two.
# - After the loop completes, the function returns the nth Fibonacci number and the step count.
# - The main part of the program asks for user input to get the position of the Fibonacci number.
# - It then calls the `fibonacci` function and prints the calculated Fibonacci number along with step count.

# Q&A Section

# Q1: What is the purpose of the `fibonacci` function?
# A1: It calculates the nth Fibonacci number and counts the number of steps taken.

# Q2: Why do we initialize `a` and `b` to 0 and 1?
# A2: `a` and `b` represent the first two numbers in the Fibonacci sequence.

# Q3: What does `a, b = b, a + b` do?
# A3: It updates `a` and `b` to the next two numbers in the sequence.

# Q4: How does the `step_count` variable work?
# A4: It increments by 1 in each loop iteration to count the steps taken to reach the nth Fibonacci number.

# Q5: What does `int(input(...))` do in the program?
# A5: It prompts the user for input, converts it to an integer, and assigns it to `n`.

# Q6: What happens if the user enters a non-integer input?
# A6: The program will raise a ValueError if the input is not an integer.

# Q7: Why do we return `a` and `step_count` from the `fibonacci` function?
# A7: `a` contains the nth Fibonacci number, and `step_count` gives the total number of steps taken.

# Q8: How is the nth Fibonacci number displayed to the user?
# A8: Using the `print` function, it shows both the Fibonacci number and the step count on the console.

# Q9: How does this iterative approach differ from a recursive approach?
# A9: The iterative approach is more efficient and avoids the overhead of multiple function calls, which are required in a recursive approach.

# Q10: What is the time complexity of this Fibonacci program?
# A10: The time complexity is O(n), as the program calculates each Fibonacci number in a single loop.

# Example of Input:
# Suppose the user enters 5.
# Output:
# The 5th Fibonacci number is: 5
# Total steps taken to compute: 5
