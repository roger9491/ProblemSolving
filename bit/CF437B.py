""" 
https://codeforces.com/contest/437/problem/B

Solution:
    1. 

湊出 limit 的 二進位

"""

def lowbit(number):
    index = 1
    low_bit = 1
    while number >> (index - 1) != 0:
        if number & low_bit != 0:
            return low_bit
        low_bit = low_bit << 1
        index += 1

sum, limit = list(map(int, input().split()))


ans = []
for i in range(limit, 0, -1):
    if sum == 0:
        break
    
    low_bit = lowbit(i)
    if sum - low_bit < 0:
        continue

    sum -= low_bit
    ans.append(i)
    
 
if sum != 0:
    print(-1)   
else:
    print(len(ans))
    print(*ans, sep=" ")
    
    
    
    

















    
        
        
        
""" 
5
101

1
1

3
11


5
101


"""
        
        
        
        
        
    
# 10 => 1010 => 10 => 1010 / 4
# print(10 >> 2) # 2

# 1010 & 10 
# 1010 & 11
# print(10 & 2)

# 10 => 1010 => 1010 00 => 1010 * 100
# print(10 << 2) # 40