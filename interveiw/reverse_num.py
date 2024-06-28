num= int(input("eneter the number"))
rev=0
while(num>0):
    dight= num%10
    rev=rev*10+dight
    num=num/10
    
    
print("reverse of the number is",rev)