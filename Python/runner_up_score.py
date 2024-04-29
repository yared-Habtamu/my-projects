if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    p=list(arr)
    x=sorted(p,reverse=True)
    z=list(set(x))
    print(z[1])
