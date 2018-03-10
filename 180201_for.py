# -*- coding: utf-8 -*-
from collections import Iterable

for i in range(1, 5):
    print(i)
else:
    print('the for loop is over')

d = {'a': 1, 'b': 2, 'c': 3}
for value in d:
    print(d[value], end=' ')
for ch in 'abc':
    print(ch, end=' ')
print()
print(isinstance('abc', Iterable))  # str是否可迭代

for x, y in [(1, 1), (2, 2), (3, 3)]:
    print(x, y)

my_list_2 = [x * x for x in range(1, 11)]
print(my_list_2)

my_list = [x * x for x in range(1, 11) if x % 2 == 0]
print(my_list)

my_list_3 = [m + n for m in 'abc' for n in 'zxc']
print(my_list_3)

l = ['a', 'B', 'C']
my_list_4 = [s.lower() for s in l]
print(my_list_4)

# 创建出generator 保存的是算法
g = (x * x for x in range(10))
print(next(g))
for n in g:
    print(n,end=' ')
print()

# break 用以中断循环语句
while True:
    s = input('enter something: ')
    if s == "quit":
        break
    print('Length of the string is', len(s))
print('done')

# continue 语句用以告诉 Python 跳过当前循环块中的剩余语句，并继续该循环的下一次迭代。
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
