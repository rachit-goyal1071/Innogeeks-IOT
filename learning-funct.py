T=int(input())
for i in range(0,T):
    s=str(input())
    n=0
    if s in "A":
        n=n+1
    elif s in "D":
        n=n-1
if n>0:
    print("Anton")
elif n<0:
    print("Dakin")
else:
    print("Friendship")