'''
question:使用正则表达式对一段文本做匹配，在匹配时能够跨越多行。
'''

# 句点（.）来匹配任意字符串，
import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is comment */'
text2 = '''/* this is a
              multiline comment */
'''

print(comment.findall(text1))  # [' this is comment ']
print(comment.findall(text2))  # []

# 解决这个问题可以添加换行符的支持
comment1 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment1.findall(text2))
# [' this is a\n              multiline comment ']
