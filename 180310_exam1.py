# -*- coding: utf-8 -*-

# try:的语句出现异常才会执行except后的语句，如果正常，则执行完try后执行else。另外，finally语句不管有无异常都会执行
a = 1
try:
    a += 1
except:
    a += 1
else:
    a += 1
finally:
    a += 1
print (a)


def bar(multiple):
    def foo(n):
        return multiple ** n
    return foo

print(bar(2)(3))


names1 = ['Amir', 'Barry', 'Chales', 'Dao']
if 'amir' in names1:
    print (1)
else:
    print (2)


counter = 1
def doLotsOfStuff():
    global counter
    for i in (1, 2, 3):
        counter += 1
doLotsOfStuff()
print (counter)