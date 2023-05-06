'''
question:我们需要以不区分大小写的方式在文本中进行查找，可能还需要做替换。
'''

# re.IGNORECASE 标记
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
# str.replace() = re.sub()
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

# 支撑函数（support function）,目的：待替换的文本与匹配的文本大小写吻合
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()  #word.capitalize() = word.title()
        else:
            return word
    return replace

print(re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE))
