# 有两个字典，我们想找出它们中间可能相同的地方
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Find keys in common
print(a.keys() & b.keys())  # {'x','y'}

# find keys in a that are not in b
print(a.keys() - b.keys())  # {'z'}

# find (key,value) pairs in common
print(a.items() & b.items())  # {('y',2)}
