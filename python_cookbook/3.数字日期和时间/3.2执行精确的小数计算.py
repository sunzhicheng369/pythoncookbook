'''
question:对小数进行精确计算，不希望因为浮点数天生的误差而带来的影响。
'''
#示例：
a = 4.2
b = 2.1
c = a + b
print(c)
print(c == 6.3)
# 这些误差实际上是底层CPU的浮点运算单元和IEEE754浮点数算术标准的一种特性。

#decimal模块提高精度,主要功能是控制计算过程的各个方面
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
c = a + b
print(c)
print(c == Decimal('6.3'))

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)

