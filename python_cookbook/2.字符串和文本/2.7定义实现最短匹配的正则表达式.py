'''
question:我们正在尝试用正则表达式对文本模式做匹配，但识别出来的是最长的可能匹配。相
反，我们想将其修改为找出最短的可能匹配
'''

# 这个问题通常会在匹配的文本被一对开始和结束分隔符包起来的时候出现
import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
# ['no." Phone says "yes.']

# 完善上述
str_pat1 = re.compile(r'\"(.*?)\"')
print(str_pat1.findall(text2))
# ['no.', 'yes.']
