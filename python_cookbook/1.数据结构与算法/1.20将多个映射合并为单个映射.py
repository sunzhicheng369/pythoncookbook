'''
question:我们有多个字典或映射，想在逻辑上将它们合并为一个单独的映射结构，以此执行某
些特定的操作，比如查找值或检查键是否存在。
'''

# 1.collections模块中的ChainMap类
a = {'x': 1, 'z': 2}
b = {'y': 2, 'z': 4}
d = {'x': 9, 'd': 5}

#ChainMap 只是简单地维护一个记录底层映射关系的列表
from collections import ChainMap
c = ChainMap(a, b, d)
print(c)
#ChainMap({'x': 1, 'z': 2}, {'y': 2, 'z': 4}, {'x': 9, 'd': 5})
print(c['x'])
