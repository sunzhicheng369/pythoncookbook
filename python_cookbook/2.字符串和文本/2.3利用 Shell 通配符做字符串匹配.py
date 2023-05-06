'''
question:当工作在 UNIX Shell 下时，我们想使用常见的通配符模式（即，*.py、Dat[0-9]*.csv
等）来对文本做匹配
'''

# fnmatch 模块提供了两个函数—fnmatch()和 fnmatchcase()
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt','*.txt'))
print(fnmatch('foo.txt','?oo.txt'))
print(fnmatch('Dat45.csv','Dat[0-9]*'))

