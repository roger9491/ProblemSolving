""" 
https://codeforces.com/contest/88/problem/C


"""

a, b = map(int, input().split())

a_list = []
b_list = []

for i in range(1, b + 1):
    a_list.append(a * i)
    
for i in range(1, a + 1):
    b_list.append(b*i)
    
seta = set(a_list)
setb = set(b_list)
com = seta.intersection(setb)

if abs(len(a_list) - len(b_list)) == len(com):
    print("Equal")
elif len(a_list) - len(b_list) > len(com):
    print("Dasha")
else:
    print("Masha")     



# print(a_list, b_list)    

# 扣掉一樣的