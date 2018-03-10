# -*- coding: utf-8 -*-

import pickle

# 用户输入内容
def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)
something = input('enter text: ')
if is_palindrome(something):
    print('yes, this is palindrome')
else:
    print('no, this is not a palindrome')

# 再议input
birth=input('brith:')
if int(birth)<2000:
    print('00前')
else:
    print('00后')



# 文件
poem ='''
Programming is fun
When the work is done

if you wanna make your work also fun:
use Python!
'''
# 打开模式，有
# -'r' 阅读模式
# -'w' 写入模式
# -'t' 文本模式
# -'b' 二进制模式

f=open('poem.txt','w')
f.write(poem)
f.close()

f=open('poem.txt')
while True:
    line=f.readline()
    # 当空字符串返回时，说明到达到了文件末尾
    if len(line) == 0:
        break
    print(line,end='')
f.close()

# pickle

shoplistfile = 'shoplist.dara'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
# Dump the object to a file
pickle.dump(shoplist, f)
f.close()
# Destroy the shoplist variable
del shoplist
# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)










