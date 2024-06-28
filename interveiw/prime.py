num=int(input("eneter "))
if num <=1:
    print(f"{num}is not an prime")
elif num == 2:
    print(f"{num} is prime")
    
else:
    for i in range(2,int(num**0.5)+1):
        if num%i ==0:
            print(f"{num} is not prime")
            break
        else:
            print("prime")
    