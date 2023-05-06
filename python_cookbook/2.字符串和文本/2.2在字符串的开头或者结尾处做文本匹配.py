'''
question:我们需要在字符串的开头或结尾处按照指定的文本模式做检查，例如检查文件的扩展
名、URL 协议类型等
'''

# str.startswith() and str.endswith()
filename = 'spam.txt'
print(filename.endswith('.txt'))  # True

url = 'htpp://www.python.org'
print(url.startswith('htpp:'))  # True

#正则表达式
import re
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:',url))
