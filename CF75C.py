""" 
https://codeforces.com/contest/75/problem/C

"""
def divisor(a, b):
    factors = []
    
    divmod = 2
    while a != 1 and b != 1:
        
        while a % divmod == 0 and b % divmod == 0:
            factors.append(divmod)
            a /= divmod
            b /= divmod
        
        divmod += 1
    return factors



a, b = map(int, input().split())
n = int(input())

factors = divisor(a, b)
print(factors)


# 先選一個數 在試 兩個數 ....
for i in range(n):
    low, heigh = map(int, input().split())
    
    n = 1
    while True:
        