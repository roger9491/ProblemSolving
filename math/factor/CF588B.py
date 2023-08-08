""" 
B. Duff in Love
https://codeforces.com/contest/588/problem/B?mobile=false


Solution:
    If a number X is prime,
    then X cannot be divided by any integer n ranging from 2 to the square root of X.
    So we can find all the prime factors of X, 
    and the anser is the product of the prime factors.

hard, 8/10

"""

n = int(input())

prime = []
tmp = n
div = 2
while tmp != 1:
    if tmp % div != 0:
        div += 1
        if div > int(tmp ** 0.5):
            prime.append(tmp)
            break
        continue

    for i in prime:
        if div % i == 0:
            break
    else:
        prime.append(div)

    while tmp % div == 0:
        tmp //= div
    div += 1

if len(prime) == 0:
    print(n)
else:
    total = 1
    for p in prime:
        total *= p
    print(total)


