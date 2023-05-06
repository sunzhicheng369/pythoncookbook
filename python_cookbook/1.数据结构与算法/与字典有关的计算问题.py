# 问题：在字典上对数据执行各式各样的计算
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
#zip()反转字典的键或者是值。
min_price = min(zip(prices.values(),prices.keys()))
print(min_price)

max_price = max(zip(prices.values(),prices.keys()))
print(max_price)
#或者对数据进性排序
prices_sorted = sorted(zip(prices.values(),prices.keys()))
print(prices_sorted)
#zip()创建了一个迭代器，他的内容只能被消耗一次。
prices_and_names = zip(prices.values(),prices.keys())
print(min(prices_and_names))
#print(max(prices_and_names))
#ValueError: max() arg is an empty sequence