# Recursive function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # function calling itself

# Taking input from user
num = int(input("Enter a number: "))

# Calling the function and displaying the result
print("Factorial of ",num,"is: ",factorial(num))
