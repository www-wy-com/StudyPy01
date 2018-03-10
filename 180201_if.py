# -*- coding: utf-8 -*-

number=int(23)
guess = int(input('enter the integer: '))

if guess == number:
    print('Congratulations, you guessed it.')
elif guess < number :
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')

#Python 中不存在 switch 语句。你可以通过使用 if..elif..else 语句来实现同样的事情

