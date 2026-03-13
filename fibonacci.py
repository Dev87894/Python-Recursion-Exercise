def fibo(num):
    if num == 0:
        return 0
    elif(num == 1):
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)
        
num = int(input("Enter number at which you want to print fibonacci series : "))
result = []
for i in range(num):
    result.append(fibo(i))

print(result)