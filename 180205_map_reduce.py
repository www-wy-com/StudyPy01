# -*- coding: utf-8 -*-
from functools import reduce


def f(x):
    return x * x


# map()传入的第一个参数是f，即函数对象本身
# 第二个是Iterable

r = map(f, [1, 2, 3, 4, 5])
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5])))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7]))


def fn(x, y):
    return 10 * x + y


print(reduce(fn, [1, 2, 3, 4]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '1358')))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


# filter 过滤序列

def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['a', '', ' ', 'b', None])))





