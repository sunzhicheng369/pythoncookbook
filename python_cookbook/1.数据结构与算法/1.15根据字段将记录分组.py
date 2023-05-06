'''
问题：有一系列的字典或对象实例，我们想根据某个特定的字段（比如说日期）来分组迭代数据。
'''
# 解决方法：itertools.groupby()函数
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
#假设根据日期以分组的方式迭代数据
from operator import itemgetter
from itertools import groupby

#sort by the desired field first
rows.sort(key=itemgetter('date'))

#Iterate in groups
for date, items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ',i)