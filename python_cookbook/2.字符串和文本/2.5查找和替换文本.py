'''
question:想对字符串中的文本做查找和替换
'''

# 对简单文本 str.replace()
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))
# yep, but no, but yep, but no, but yep

# 针对更复杂的模式，可以使用re模块中的sub（）函数、方法。
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re

# sub()的第 1 个参数是要匹配的模式，第 2 个参数是要替换上的模式
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# Today is 2012-11-27. PyCon starts 2013-3-13.
