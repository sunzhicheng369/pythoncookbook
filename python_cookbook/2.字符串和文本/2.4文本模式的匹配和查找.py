'''
question: 想要按照特定的文本模式进行匹配或查找。
'''
# 方法:想要匹配的只是简单的文字，那么通常只需要用基本的字符串方法就可以了。

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
print(text == 'yeah')

# March at start or end
print(text.startswith('yeah'))

# search for the location of the first occurrence
print(text.find('no'))

# 对于更为复杂的匹配则需要使用正则表达式以及re模块。
text1 = '11/27/2012'
text2 = 'Nov 27,2012'

import re

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

# match()方法总是尝试在字符串的开头找到匹配项
datepat = re.compile(r'\d+/\d+/\d+')  # 正则表达式

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))  # findall()方法搜索整个文本并找出所有的匹配项然后将它们以列表的形式返回
