n, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

left, right = 1, 10**9
res = -1

while left <= right:
    mid = (left + right) // 2
    count = 0

    for num in nums:
        if num <= mid:
            count += 1
    if count == k:
        res = mid
        break
    elif count < k:
        left = mid + 1
    else:
        right = mid - 1

print res
