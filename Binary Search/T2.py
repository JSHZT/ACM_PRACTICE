def is_fine(nums, t, m, n):
    i = 0
    temp = t
    count = 0
    while count < m and i < n:
        while temp > 0 and i < n:
            temp -= nums[i]
            i += 1
            if temp < 0:
                i -= 1
                break
        count += 1
        temp = t
    if i < n:
        return False
    return True
                

while True:
    try:
        n, m = map(int, input().split())
        nums = list(map(int, input().split()))
        T_max = sum(nums) + 1 // m
        if T_max < max(nums):
            print(-1)
        l = max(nums)
        while l < T_max:
            mid = l + ((T_max - l) >> 1)
            if is_fine(nums, mid, m, n):
                T_max = mid - 1
            else:
                l = mid + 1
        print(l)
    except:
        break