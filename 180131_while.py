# -*- coding: utf-8 -*-


# while
# for x in ...循环就是把每个元素代入变量x

numbers =[12,37,5,42,8,3]
even =[]
odd = []
while len(numbers)> 0 :
    number = numbers.pop()
    if(number  % 2 == 0 ):
        even .append(number)
    else:
        odd. append(number)
print(numbers)
print(odd)
print(even)

# 计算1-100的和
sum = 0
for x in range(101):
    sum = sum + x
print('sum of 1-100 is:',sum)

# 计算1——100之和
sum=0
num=100
while num>0:
    sum=sum+num
    num=num-1
print('sum of 1-100 is:',sum)


# continue
i= 1
while i<10:
    i+=1
    if i%2==0 :
        continue
    print (i)

#break
i = 1
while 1:
    print(i)
    i+=1
    if i>10:
        break

# input
var = 1
while var<4:  # 该条件永远为true，循环将无限执行下去
    var=var+1
    num = input('Enter a number  :')
    print ("You entered: ", num)














