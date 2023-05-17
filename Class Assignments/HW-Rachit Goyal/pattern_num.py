n=int(input())
for a in range(1,n+1):
    for b in range(1,n+1):
        print((' '*(n-b)),b,(' '*(n-a)),end=" ")
        if a==b:
            break
    print()