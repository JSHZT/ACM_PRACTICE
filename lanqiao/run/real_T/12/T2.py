line_set = set()
p = []
m = 20
n = 21
for i in range(m):
    for j in range(n):
        p.append([i, j])

for i in p:
    for j in p:
        if i[0]==j[0] or j[1]==i[1]:
            continue
        k = (j[1]-i[1])/(j[0]-i[0])
        b = i[1] - k * i[0]
        k = round(k, 4)
        b = round(b, 4)
        
        line_set.add((k, b))
print(len(line_set)+m+n)

