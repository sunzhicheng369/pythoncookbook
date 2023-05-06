'''
问题：我们的代码已经变得无法阅读，到处都是硬编码的切片索引，我们想将它们清理干净。
'''

# record = '....................100 .......513.25 ..........'
# cost = int(record[20:32]) * float(record[40:48])

# slice()函数会创建一个切片对象，可以用在任何允许进行切片操作的地方

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])  # [2, 3]
print(items[a])  # [2, 3]
# 以分别通过 s.start、s.stop 以及 s.step 属性来得到关于该对象的信息
print(a.start)
print(a.step)
print(a.stop)

# indices(size)方法将切片映射到特定大小的序列上
s = 'HelloWorld'
print(a.indices(len(s)))


