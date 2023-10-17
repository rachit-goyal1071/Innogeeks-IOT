a=int(input("enter value in: "))
c=int(input("enter value in: "))
b=int(input("enter value in: "))
if a>b :
    if b>c:
        print("median is", b)
    elif c>a:
        print("median is", a)
    else:
        print("median is",c)
elif c>b:
    print("median is", b)
elif c>a:
    print("median is",c)
else:
    print("median is",a)