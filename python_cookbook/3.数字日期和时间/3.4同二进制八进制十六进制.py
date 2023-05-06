'''
question:二进制，八进制，十六进制表示数值或者转换
'''
x = 1234

#二进制
print(bin(x))
#0b10011010010
print(format(x,'b'))
#10011010010

#八进制
print(oct(x))
#0o2322
print(format(x,'o'))
#2322

#十六进制
print(hex(x))
#0x4d2
print(format(x,'x'))
#4d2