""" 
https://codeforces.com/contest/296/problem/C

3 3 3
1 2 3
1 2 1
1 3 2
2 3 4
1 2
1 3
2 3

9 18 17


1 2 3

1 2 1
2 3 3

1 3 2

4 5 5

1 2 1

5 6 5

1 3 2

7 8 7

2 3 4

7 12 11

1 3 2

9 14 13

2 3 4

9 18 17
---------
operation
3 3 3
1 2 3
1 2 1
1 3 2
2 3 4
1 2


[1, 1, 1]
1 2 1
1 3 2

[2, 1, 0]
[4, 1, 0]

4 5 5


1 2 3
1 2 1
1 3 2

[4, 4, 3]
[2, 3, 3]
[4, 5, 5]
"""
def fn(finite_dif):
    ans = []
    tmp = 0
    for i in range(len(finite_dif)):
        tmp += finite_dif[i]
        ans.append(tmp)
    return ans


n, m, k = map(int, input().split())
a = list(map(int, input().split()))

finite_dif = []
for i in range(len(a)):
    if i == 0: 
        finite_dif.append(a[i])
        continue
    
    finite_dif.append(a[i] - a[i - 1])
    

operation = []
for i in range(m):
    l, r, d = map(int, input().split())
    operation.append([l, r, d])

for i in range(k):
    x, y = map(int, input().split())
    print(x, y)
    print("原本", finite_dif)
    print("還原", fn(finite_dif))
    
    
    for j in range(x - 1, y):
        finite_dif[operation[j][0] - 1] += operation[j][2]
        
        if operation[j][1] < len(finite_dif) - 1:
            finite_dif[operation[j][1]] -= operation[j][2]
        print(operation[j][0], operation[j][1], operation[j][2])
        print(finite_dif)
        print(fn(finite_dif))
    
    

        
ans = []
tmp = 0
for i in range(len(finite_dif)):
    tmp += finite_dif[i]
    ans.append(tmp)
    
print(*ans, sep=" ")
    
    
        