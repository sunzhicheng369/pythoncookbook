'''
问题:去除序列中出现的重复元素，但仍然保持剩下的元素顺序不变
'''


# 方法一：如果序列中的值是可哈希的，通过使用集合和生成器。

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# 方法二：如果序列是不可哈希的对象
def dedupe(items, key=None):  # key的作用，指定一个函数用来将序列中的元素转换为可哈希类型
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(b, key=lambda d: (d['x'], d['y']))))

# 只是去除重复项，最简单的方法就是直接构建一个集合
print(set(a))  # 这种方法不能保证元素间的顺序不变
# {1, 2, 5, 9, 10}
