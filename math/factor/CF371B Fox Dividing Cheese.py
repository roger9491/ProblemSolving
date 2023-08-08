""" 
https://codeforces.com/contest/371/problem/B


Solution:
    This problem involvs two numbers, and the goal is
    to make them equal by using division.
    So, the first thing that comes to my mind is factor.
    Becaues, the all number are composed of factors.
    When the facotors composing the two numbers are the same,
    the numbers are equal.
"""
a, b = map(int,input().split(' '))

aMap = {}
bMap = {}
g = [2, 3, 5]
for i in g:
    aMap[i] = 0
    bMap[i] = 0
flag = 0
ans = 0
for i in g:
    while a % i == 0:
        a = a // i
        aMap[i] += 1 
    while b % i == 0:
        b = b // i
        bMap[i] += 1 
for i in g:
    ans += abs(aMap[i] -  bMap[i])

if a != b:
    print(-1)
else:   
    print(ans)
# 21 35
        
