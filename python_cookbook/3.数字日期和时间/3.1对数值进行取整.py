'''
question: 将一个浮点数取整到固定的小数位。
'''
# round(value,ndigits)函数
print(round(1.23, 1))
print(round(-1.27, 1))

# 传递给round()的参数ndights可以是负数，在此情况下会响应的去取整到十位，百位。
a = 1627731
print(round(a, -1))

# 格式化
x = 1.23456
print(format(x, '0.2f'))
