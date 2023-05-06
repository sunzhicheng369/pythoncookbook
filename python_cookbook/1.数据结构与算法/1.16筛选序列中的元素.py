'''
问题：序列中有一些数据，我们需要提取出其中的值或根据某些标准对序列做删减
'''

# 解决方法：列表推导式
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])

print([n for n in mylist if n < 0])
# 使用列表推到式的一个潜在缺点是如果原始输入非常大的话，可能会产生一个庞大的结果
# 可以使用生成器表达式方式
pos = (n for n in mylist if n > 0)
print(pos)

# 假设筛选过程涉及异常处理或者其他一些复杂的细节--filter()函数。
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))  # filter()创建了一个迭代器
print(ivals)

'''
filter()函数用于过滤序列，过滤掉不符合条件的元素，返回符合条件的元素组成新列表。
filter(function,iterable)

function -- 判断函数。
iterable -- 可迭代对象
'''
import math

print([math.sqrt(n) for n in mylist if n > 0])

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

# -----itertools.compress()
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)

print(list(compress(addresses,more5)))
#compress()函数挑选出满足布尔值为 True 的相应元素