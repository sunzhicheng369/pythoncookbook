'''
question: 一个字节串，需要将其解包为一个整数，将一个大整数重新转化为一个字节串。
'''

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

#要将字节解释为整数，可以使用int.from_bytes()
print(len(data))
print(int.from_bytes(data,'little'))
print(int.from_bytes(data,'big'))

#要将一个大整数重新转化为字符串
x = 94522842520747284487117727783387188
print(x.to_bytes(16,'big'))
print(x.to_bytes(16,'little'))
