# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(input().split())
m = int(input())
b = set(input().split())
print(len(a.union(b)))
