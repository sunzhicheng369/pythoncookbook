'''
queston:我们需要调用一个换算（reduction）函数（例如 sum()、min()、max()），但首先得对数
据做转换或筛选。
'''
# 方式一：生成器
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

#determine if any .py files exist in a directory
# import os
# files = os.listdir('dirname')
# if any(name.endswith('.py') for name in files):
#     print('there be python')
# else:
#     print('sorry, no python')

# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
#original:returns 20
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

## Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)