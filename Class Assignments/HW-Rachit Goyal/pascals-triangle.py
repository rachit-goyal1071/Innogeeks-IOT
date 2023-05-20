n=int(input())
for a in range(n-1,0,-1):
    print(" "*a,end=" ")
    for b in range(1,(n-a)+1):
        print(b,end="")
    for c in range(((n-a)-1),0,-1):
        print(c,end="")
    print()