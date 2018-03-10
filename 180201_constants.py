# -*- coding: utf-8 -*-


# format(value, format_spec='', /)
# Return value.__format__(format_spec)
# format_spec defaults to the empty string.
# See the Format Specification Mini - Language section of help('FORMATTING') for details.
# 一些字符串可以使用特定的格式，format可以使相应的参数替代这些格式
# python从零开始计数

name='mike'
age=20

print('{0} was {1} years old ,when he wrote this book'.format(name,age))
print('he was {0} years old'.format(age))

# Python 中 format 方法所做的事情便是将每个参数值替换至格式所在的位置。这之中可以有更详细的格式
# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print('a',end='')
print('b',end=' ')
print('c',end='')

print('This is the first line\nThis is the second line')


name='swaroop'
if name.startswith('swa'):
    print('yes,the string starts with swa')
if 'a' in name:
    print('yes,it contains the string a')
if name.find('ar')!=-1:
    print('yes,it contains the string ar')
delimiter ='_*_'
mylist =['a','b','c']
print(delimiter.join(mylist))




























