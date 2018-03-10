# -*- coding: utf-8 -*-

# 四种内置的数据结构
# - list : mutable
# - tuple :
# - dictionnary
# - set

# this is a shopping list
shoplist=['apple','manggo','carrot']
print('i have',len(shoplist),'item to purchase')
print('this items are:',end=' ')
for item in shoplist:
    print(item,end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('My shopping list is now', shoplist)

print('the first item i buy is',shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print('i bought the',olditem)
print('My shopping list is now', shoplist)

print('the shopping list has {} items'.format(len(shoplist)))
print('the last one in shopping list is {}'.format(shoplist[-1]))


print('***************************************')

# this is tuple
# 不能编辑、更改元组
zoo = ('python', 'elephant', 'penguin')
print('number of animals in the zoo is',len(zoo))

new_zoo=('monkey','camel',zoo)
print('Number of cages in the new zoo is', len(new_zoo))
print('number of cages in new zoo is',len(new_zoo))
print('all animals in new zoo are',new_zoo)
print('animals brougt from old zoo are',new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))


t=('a','b',['c','d'])
t[2][0]='x'
t[2][1]='y'
print(t)
print('***************************************')





# this is dictionary
# 将key 和 values 相联系一起
ab={
    'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'
}
print("Swaroop's address is", ab['Swaroop'])

# 删除一对键-值配对
del ab['Spammer']
print('there are {} contacts in the address-book\n'.format(len(ab)))
for name,addresss in ab.items():
    print('contact {} at {}'.format(name,addresss))
# add
ab['guido']='guido@python.org'
if 'guido' in ab:
    print("\nguido's address is", ab['guido'])

#sequence
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# Indexing or 'Subscription' operation #
# 索引或“下标（Subcription）”操作符 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])
# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])
# 从某一字符串中切片 #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
print('***************************************')

# inference
myshoplist=['a','b','c']

print('single assignment')
mylist=myshoplist

del myshoplist[0]
print('myshoplist is: ',myshoplist)
print('mylist is: ',mylist)
# 都打印出了没有a的列表，说明他们指向同一个对象

print('copy by making a full slice')
mylist=myshoplist[:]
del myshoplist[0]
print('myshoplist is: ',myshoplist)
print('mylist is: ',mylist)
# 此时两份list出现了不同