# 1. Sum of First N Natural Numbers
def add(n):
    if n < 0:
        return "Invalid input! Number should be greater than 0"
    elif n == 1:
        return 1
    else:
        return n + add(n - 1)

num = int(input("Enter number to get its factorial : "))        
result = add(num)
print(result)


# 2. Reverse a String
def reverse_string(text):
    if len(text) <= 1:
        return text
    else:
        return text[-1] + reverse_string(text[: -1])


text = input("Enter text to reverse it : ")
result = reverse_string(text)
print(result)


# 3. Reverse a number.
def reverse_number(num, rev = 0):
    if num == 0:
        return rev
    else:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
        return reverse_number(num, rev)
    
num = int(input("Enter a number : "))
reverse = reverse_number(num)
if reverse == num:
    print(f"given number = {num}\nreversed number = {reverse}")
    print("The number is palindrome.")
else:
    print(f"given number = {num}\nreversed number = {reverse}")
    print("The number is not palindrome.")
print(reverse)
    
    
# 4. Check number is palindrome.
def reverse_number(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return reverse
num = int(input("Enter a number : "))
reverse = reverse_number(num)
if reverse == num:
    print(f"given number = {num}\nreversed number = {reverse}")
    print("The number is palindrome.")
else:
    print(f"given number = {num}\nreversed number = {reverse}")
    print("The number is not palindrome.")


# 5. Print N to 1
def natural_numbers(num):
    if num == 0:
        return
    else:
        natural_numbers(num-1)
        print(num)
num = int(input("Enter how natural numbers you want : "))
natural_numbers(num)
