'''
question:对大型数据集比如数组或者是网格（grid）进行计算。
'''

# 数组与列表的区别
# python lists
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print(x * 2)
# [1, 2, 3, 4, 1, 2, 3, 4]
print(x + y)
# [1, 2, 3, 4, 5, 6, 7, 8]

# numpy arrays
import numpy as np

ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])

print(ax * 2)
# [2 4 6 8]
print(ax + ay)
#[ 6  8 10 12]

