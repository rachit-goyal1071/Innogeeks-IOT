# cook your dish here
T=int(input())
for j in range(0,T):
    a=0
    b=1
    N=int(input())
    S=str(input().split())
    # if type(S)==str:
    for i in range(1,N+1):
            if S[i]  not in ["a","e","i","o","u"]:
                a+=1
                b=b+i
                if b==((i-3)*2):
                    print("NO")
                    a=a+10
                    exit()
                else:
                    print("YES")
                    exit()
        
                
        # if (N-a)>=4:
        #     print("NO")
        # else:
        #     print("YES")
    # else:
    #     print("YES")