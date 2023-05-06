'''
quetion:对数值进行格式化处理，包括控制制位符，对齐，包括千位分隔符。
'''
# 对一个单独的数字做格式化输出，使用内建的format()函数即可。
x = 1234.56789

# two decimal places of accuracy
print(format(x, '0.2f'))

# right justifield in 10 chars, one-digit accuracy
print(format(x,'>10.1f'))

#Inclusion of thousands separator
print(format(x, ','))

#科学计数法
print(format(x, 'e'))
print(format(x,'0.2E'))