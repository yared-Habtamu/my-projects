n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans=""
fast=0
for slow in range(len(b)):
    while fast<len(a) and a[fast]<b[slow]:
        fast+=1
    ans+=(str(fast))
    ans+=' '

print(ans.strip())
    
# I used two pointers fast and slow using for- while loop combo
