n = int(input())
height_list = list(map(int, input().split()))
lens = len(height_list)
l = [-1] * lens
r = [-1] * lens

stack = []
for i in range(lens-1, -1, -1):
    while stack and stack[-1] <= height_list[i]:
        stack.pop()
    if stack:
        r[i] = height_list.index(stack[-1]) + 1
    stack.append(height_list[i])
stack.clear()
for i in range(lens):
    while stack and stack[-1] <= height_list[i]:
        stack.pop()
    if stack:
        l[i] = height_list.index(stack[-1]) + 1
    stack.append(height_list[i])
for i in l:
    print(i, end=' ')
print('')
for i in r:
    print(i, end=' ')
