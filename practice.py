
num = int(input("enter the number :"))
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
fact =factorial(num)
print(f"factorial of {num} is {fact}")  
# ✅ Using Recursion:
num =int(input("enter the number :"))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
f= factorial(num)  
print(f"factorial of {num} is {f}")




# By messaging ChatGPT, you agree 



import math

# Step 1: Ask the user for a number
try:
    num = float(input("Enter a number: "))

    # Ensure the number is positive for square root and logarithm
    if num < 0:
        print("Please enter a non-negative number for square root and logarithm.")
    else:
        # Step 2: Calculate square root
        sqrt_num = math.sqrt(num)
        print(f"Square root of {num}: {sqrt_num}")

        # Step 3: Calculate natural logarithm
        log_num = math.log(num)
        print(f"Natural logarithm of {num}: {log_num}")

        # Step 4: Calculate sine (assuming the number is in radians)
        sine_num = math.sin(num)
        print(f"Sine of {num} radians: {sine_num}")

except ValueError:

    print("Invalid input! Please enter a valid number.")
