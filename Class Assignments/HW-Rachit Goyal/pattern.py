n=int(input())
for a in range(1,n+1):
    print((' '*(n-a)),"*"*((2*a)-1),(' '*a))
for a in range(n-1,0,-1):
    print((' a '*(n-a)),"*"*((2*a)-1),(' '*a))
