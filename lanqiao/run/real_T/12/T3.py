import math
n = 2021041820210418
set1 = set()

for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
        set1.add(i)
        set1.add(n // i)
        
ans = 0
for i in set1:
    for j in set1:
        for k in set1:
            if i*j*k==n:
                ans += 1
print(ans)