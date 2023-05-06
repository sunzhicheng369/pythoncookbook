'''
问题：元素序列，想知道在序列中出现次数最多的元素是什么。
'''
#解决方案:collections 模块 counter类。
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
words_counts = Counter(words)
print(words_counts)
top_three = words_counts.most_common(3)
print(top_three)  #[('eyes', 8), ('the', 5), ('look', 4)]

#可以给counter对象提供任何可哈希的对象列表作为输入，在底层实现中，counter是一个字典
#在元素和他们出现的次数做了映射。
print(words_counts['not'])