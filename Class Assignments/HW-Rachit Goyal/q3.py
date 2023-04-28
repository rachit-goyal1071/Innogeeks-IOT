a=0
b=1
n=int(input("enter no"))
for i in range (0,n):
    sum=a+b
    a=b
    b=sum
    print(a)
