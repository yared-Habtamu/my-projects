n,k=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
ans=[]
i,j=0,0
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        ans.append(arr1[i])
        i+=1
    else:
        ans.append(arr2[j])
        j+=1

# here we only get the value of merged arrays untill i or j reaches their max first
#so we should extend the remaining part of either array
ans.extend(arr1[i:])
ans.extend(arr2[j:])

st = map(str, ans)
res = " ".join(st)

print(res)
