# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())
a = defaultdict(list)

for i in range(1, n+1):
    word = input().strip()
    a[word].append(i)

for _ in range(m):
    word = input().strip()
    if word in a:
        print(" ".join(map(str, a[word])))
    else:
        print(-1)
