'''
question:我们需要将字符串拆分为不同的字段，但是分隔符（以及分隔符之间的空格）在整个
字符串中并不一致。
'''
# spilt()函数

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re

print(re.split(r'[;,\s]\s*', line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

