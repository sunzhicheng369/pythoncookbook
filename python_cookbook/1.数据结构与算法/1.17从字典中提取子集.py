'''
问题：创建一个字典，其本身是另一个字典的子集
'''

# 解决：字典推导式
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# make a dict of all price over 200
pl = {key: value for key, value in prices.items() if value > 200}
print(pl)

# make a dict of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key : value for key,value in prices.items() if key in tech_names}
print(p2)
