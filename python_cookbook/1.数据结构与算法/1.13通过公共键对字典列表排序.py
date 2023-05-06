'''
问题：有一个字典列表，想根据一个或多个字典中的值来对列表排序。
'''
# 解决方法：operator模块中的itemgetter函数进行排序。

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

# itemgetter()函数还可以接受多个键。
row_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(row_by_lfname)

# 在这个例子中，rows被传递给内建的sorted()函数，该函数接受一个关键参数key.
# 该参数代表一个可调用对象(callable),该对象从 rows 中接受一个单独的元素作为
# 输入并返回一个用来做排序依据的值。

# 有时候会用 lambda 表达式来取代 itemgetter()的功能
#rows_by_fname = sorted(rows, key=lambda r: r['fname'])
#row_by_lfname = sorted(rows, key=lambda r: r(r['lname'], r['fname']))

# itemgetter()通常会运算的更快一些。
# 本节中所展示的技术同样适用于 min()和 max()这样的函数
print(min(rows, key=itemgetter('uid')))
