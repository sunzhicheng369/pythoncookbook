class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


import sys


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'Guido'
n = 37
print(sub('Helo {name}'))

