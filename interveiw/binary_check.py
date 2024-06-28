num = 110100102

while num > 0:
    rem = num % 10
    if rem != 0 and rem != 1:
        print("Not a binary number")
        break
    num = num // 10
else:  
    print("It is a binary number")
