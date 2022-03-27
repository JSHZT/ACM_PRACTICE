import heapq
while True:
    try:
        n = int(input())
        a_list = list(map(int, input().split()))
        heapq.heapify(a_list)
        ans = 0
        while len(a_list) > 1:
            x1 = heapq.heappop(a_list)
            x2 = heapq.heappop(a_list)
            ans += x1 + x2
            heapq.heappush(a_list, x1+x2)
        print(ans)
    except:
        break