'''
question:对浮点数的无穷大，负无穷大或者NAN(not a number)进行判断测试
'''

#python 中没有特殊的用法来表示这些特殊的浮点数值。
#检测这些值，math.isinf()和math.isnan()函数
a = float('inf')
b = float('nan')

import math

print(math.isinf(a))
print(math.isnan(b))