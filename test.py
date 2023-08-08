# 長度為 8
array = [[1,4], [2,2],[3,6],[4,1], [5,3], [6,8], [7,5], [8,7]]
target = [4, 6]
array.sort(key=lambda x: x[1])
print(array)