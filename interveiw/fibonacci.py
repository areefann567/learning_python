n=int(input("enter "))
first=0
sec=1
series=[first,sec]
if n==0:
    print(first)
else:
    for i in range(0,n-2):
        next=series[i]+ series[i+1]
        series.append(next)
        
print(series)
        