""" 
https://codeforces.com/contest/518/problem/B


"""

s = input()
t = input()

map = {}

for st in t:
    if st not in map:
        map[st] = 1
    else:
        map[st] += 1
        
ans1 = 0
ans2 = 0
temp = []
for i in s:
    if i in map and map[i] > 0:
        map[i] -= 1
        ans1 += 1
    else:
        temp.append(i)

for i in temp:
    if i.upper() in map and map[i.upper()] > 0:
        map[i.upper()] -= 1
        ans2 += 1
    elif i.lower() in map and map[i.lower()] > 0:
        map[i.lower()] -= 1 
        ans2 += 1


print(ans1, ans2)