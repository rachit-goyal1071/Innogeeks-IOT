T=int(input())
for a in range(0,T):
    X,Y=map(int,input().split())
    if (Y<=X):
        print("YES")
    else:
        print("NO")