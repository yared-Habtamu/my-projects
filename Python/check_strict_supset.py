# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())
n=int(input())
ans=True
for _ in range(n):
    b=set(input().split())
    for val in b:
        if val not in a:
            ans=False
            break;

print(ans)
