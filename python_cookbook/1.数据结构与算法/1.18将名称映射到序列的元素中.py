'''
question:我们的代码是通过位置（即索引，或下标）来访问列表或元组的，但有时候这会使代
码变得有些难以阅读。我们希望可以通过名称来访问元素，以此减少结构中对位置的
依赖性
'''
# 解决方案：
# collections.namedtuple() (命名元组)

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)  # Subscriber(addr='jonesy@example.com', joined='2012-10-19')
print(sub.addr)

# 命名元组的主要作用在于将代码同它所控制的元素位置间解耦
