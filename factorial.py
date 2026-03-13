def factorial(n):
    if n < 0:
        return "Invalid input! Number should be greater than 0"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter number to get its factorial : "))        
result = factorial(num)
print(result)