# -*- coding: utf-8 -*-

from operator import itemgetter

print(list(sorted([36, 5, -2, 9, -27])))
# sort函数也是高阶函数，可以根据key函数来实现自定义的排序
print(list(sorted([36, 5, -12, 9, -21], key=abs)))
# 实现忽略大小写的排序
print(sorted(['a', 'B', 'c', 'D'], key=str.lower))
# reverse可以实现反向排序
print(sorted(['a', 'B', 'c', 'D'], key=str.lower, reverse=True))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[0]))
print(sorted(students, key=lambda t: t[1]))

print(students[0].__getitem__(1))

