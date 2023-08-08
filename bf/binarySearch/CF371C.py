""" 
https://codeforces.com/contest/371/problem/C


Solution:

"""
s = input()
n = list(map(int, input().split()))
p = list(map(int, input().split()))
r = int(input())
c = [0]*3

for i in range(len(s)):
    if s[i] == 'B':
        c[0] += 1
    elif s[i] == 'S':
        c[1] += 1
    elif s[i] == 'C':
        c[2] += 1
totalCost = c[0]*p[0] + c[1]*p[1] + c[2]*p[2]


minv = 1000
maxv = 0
for i in range(3):
    if c[i] == 0: continue

    minv = min(minv, n[i] // c[i])
    maxv = max(maxv, n[i] // c[i] + 1)
# print(minv, maxv)

i = minv
j = maxv
while i <= j:
    mid = (i + j) // 2
    # print("mid", mid)
    cost = 0
    for x in range(3):
        if c[x] == 0: continue

        cost += p[x] * max(0, (mid*c[x] - n[x]))
    # print("cost", cost)

    if cost > r:
        j = mid - 1
    elif cost < r:
        i = mid + 1
    else:
        i = mid
        j = mid
        break
# print(i, j)
# print(r, cost, totalCost)
print(min(i, j) + max(0, (r - cost) // totalCost))





