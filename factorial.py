def factorial(n):
    # Write your code here
    # Base Case
    if n == 1 :
        return 1
    # Recursive Case
    else :
        return (n * factorial(n-1))

n = int(input("Enter a number"))
print(factorial(n))