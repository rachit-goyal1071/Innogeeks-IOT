a=input("enter no")
b=input("enter no")
c=input("enter no")
if a<=b<=c or c<=b<=a:
    print("the no. is",b)
elif b<=a<=c or c<=a<=b:
    print("the no is",a)
else:
    print("the no is",c)