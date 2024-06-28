def factorial(n):
    if n==0:
        return 1;
    else:
        return n*factorial(n-1);
    

num=4
result= factorial(num)
print(f"{num} factorial is {result}")


## using loop

def factorial1(n):
    result=1;
    for i in range(1,n+1):
        result=result*i;  
    return result

num1=4
result1= factorial1(num1)
print(f"{num1} factorial is {result1}")




