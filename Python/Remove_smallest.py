t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    if len(li)==1:
        ans.append("YES")
    z=sorted(li)
    for i in range(1,len(z)):
        dif=z[1]-z[0]
        if dif<=1:
            z.remove(z[0])
            if len(z)==1:
                ans.append("YES")
                break
        else:
            ans.append("NO")
            break
for an in ans:
    print(an)

