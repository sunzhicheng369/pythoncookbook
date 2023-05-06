'''
question:奇点问题
'''

#complex(real,imag)函数
a = complex(2, 4)  #(2+4j)
b = 3 - 5j
#实部，虚部，共轭值
print(a.real, a.imag) #2.0 4.0
print(a.conjugate())
#(2-4j)

#复数的运算
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(abs(a))

#cmath模块 ：正弦，余弦，平方根
import cmath
print(cmath.sin(a))

