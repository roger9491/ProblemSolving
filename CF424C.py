""" 
https://codeforces.com/contest/424/problem/C


3
1 2 3

3



7
1 2 3 4 6 7 8

0 1 1 3 1 0

00

01

01
---
00

11
---
11

01
---
10


7
4

0111
0100
0011


11
25

14

00001011
00011001
00010010
2 + 16

00

"""

print(7 % 6)
# n = int(input())
# p = list(map(int, input().split()))


# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == 1:
#             q = p[i - 1] ^ (i % j)
#             continue
        
#         q = q ^ (i % j)
    
#     if i == 1: 
#         ansq = q
#     else:
#         ansq ^= q

# print(ansq)