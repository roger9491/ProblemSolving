""" 
https://codeforces.com/contest/451/problem/C


5
3 0 0 0
3 3 0 0
6 4 1 0
6 3 3 0
3 3 3 2


yes
yes
yes
no
no


3 1 1 1

t1 - t2 = abs(1)
t2 - t3 = abs(1)
1. 
    t1 > t2
    t3 > t2

2. 
    t2 > t1 or t2 > t3
    
    
4 2

1. 
t2 > t3
t2 > t3

t1 > t2 * 6

2 2


6 3 3 0

t2 > t1 * 3
t3 > t2 * 3



1. 
    t2 win 
    1. d1 == d2
        ((n - k) - d1 * 2) % 3 == 0 
        ex. 
            d1 == d2 == 5
            0 5 0
            10 
    ==> 
        need: k == max_d
        yes: ((n - k) - (max_d + min_d)) % 3 == 0 
        
        
    2. d1 != d2
        d1 = 5, d2 = 2
        1. 
            7 2 0 => d2 + d1, d2, 0
            need: k == d1 + d2 + d2
            yes: ((n - k) - (d1 + d1 + d2)) % 3 == 0
        ==> 
            need: k == max_d + min_d*2
            yes: ((n - k) - (max_d*2 + min_d)) % 3 == 0
        
        2. 
            0 5 7 => 0, d1, d1 + d2
            need: k == d1 + d1 + d2
            yes: ((n - k) - (d1 + d2 + d2)) % 3 == 0
        ==> 
            need: k == max_d*2 + min_d
            yes: ((n - k) - (min_d + max_d*2)) % 3 == 0

2. 
    t1 and t3 win
    1. d1 == d2

        ex.
            d1 == d2 == 5
            5 0 5
            need: k == d1 + d2
            yes: ((n - k) - (d2)) % 3 == 0

    2. 
        d1 != d2
        
        ex.
            d1 = 5, d2 = 2
            5 0 2
            need: k == d1 + d2
            yes: ((n - k) - (d1 + (d1 - d2))) % 3 == 0
            
    ==> need: k == max_d + min_d 
        yes: ((n - k) - (max_d + (max_d - min_d))) % 3 == 0

3 2 0 1
"""

n = int(input())
for i in range(n):
    n, k, d1, d2 = map(int, input().split())

    max_d = max(d1, d2)
    min_d = min(d1, d2)
    
    if ((n - k) - (max_d + (max_d - min_d))) % 3 == 0 and (n - k) - (max_d + (max_d - min_d)) >= 0:
        print("yes")
    elif max_d == 0 and min_d == 0 and (n - k) % 3 == 0:
        print("yes")
    elif max_d == min_d and ((n - k) - (max_d + min_d) % 3 == 0):
        print("yes")
    else:
        print("no")
    
    # if k == max_d and ((n - k) - (max_d + min_d)) % 3 == 0:
    #     print("yes")
    # elif k == max_d + min_d*2 and ((n - k) - (max_d*2 + min_d)) % 3 == 0:
    #     print("yes")
    # elif k == max_d*2 + min_d and ((n - k) - (min_d + max_d*2)) % 3 == 0:
    #     print("yes")
    # elif k == max_d + min_d  and ((n - k) - (max_d + (max_d - min_d))) % 3 == 0:
    #     print("yes")
    # elif max_d == 0 and min_d == 0 and (n - k) % 3 == 0:
    #     print("yes")
    # else:
    #     print("no")
    
