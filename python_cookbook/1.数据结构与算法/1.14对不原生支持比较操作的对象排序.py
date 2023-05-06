'''
问题：在同一个类的实例之间做排序，但是它们并不原生支持比较操作
'''


# 内建的sorted()函数可接受一个用来传递调用的对象(callable)的参数key
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)
# [User(23), User(3), User(99)]

print(sorted(users, key=lambda u: u.user_id))

# 可以用 lambda 表达式外，另一种方式是使用 operator.attrgetter()
from operator import attrgetter

print(sorted(users, key=attrgetter('user_id')))

# attrgetter()要更快一些，而且具有允许同时提取多个字段值的能力
