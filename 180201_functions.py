# -*- coding: utf-8 -*-


# 全局变量




def print_max(a, b):
    if a > b:
        print(a, 'is max')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is max')


print_max(3, 4)
x = 5
y = 2
print_max(x, y)

# 局部变量
x = 50


def func_local(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func_local(x)
print('x is still', x)

# global 变量
x = 50


def func_global():
    global x
    print('z is', x)
    x = 2
    print('changed global x to', x)


func_global()
print('Value of x is', x)


# 默认参数值
def say(message, times=1):
    print(message * times)


say('Hello')
say('World', 5)


# 关键字参数
def func_keyword(a, b=5, c=5):
    print('a is', a, 'and b is', b, 'and c is', c)


func_keyword(3, 7)
func_keyword(1, c=2)
func_keyword(b=3, a=3)


# docStrings
def print_maxnum(x, y):
    """
    :param x: must be interger
    :param y: must be interger
    :return: prints the maxinum of two numbers
    """
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is max')
    else:
        print(y, 'is max')


print_maxnum(2, 3)
print(print_maxnum.__doc__)


# 可变参数
def total(a=5, *numbers, **phonebook):
    print('a', a)
    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)
    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))


def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        print(b)
        a, b = b, a + b
        n = n + 1
    return "done"


f = abs


def add(x, y, f):
    return f(x) + f(y)

















