# -*- coding: utf-8 -*-
import math


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('hello ,my name is', self.name)


person = Person('wy')
person.say_hello()


class Robot:
    """表示有一个带有名字的机器人。"""
    # 一个类变量，用来计数机器人的数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))
        # 当有人被创建时，机器人
        # 将会增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了。"""

        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候
        没问题，你做得到。"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("c-3P0")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()


class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(initialized SchoolMember :{})'.format(self.name))

    def tell(self):
        print('name :{}  age :{} '.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('initialized Teacher :{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary :{}'.format(self.salary))


class Student(SchoolMember):
    """代表一位学生。"""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('mike', 40, 30000)
s = Student('tom', 25, 75)
members = [t, s]
for member in members:
    member.tell()


def move(start_x, start_y, step, angle=0):
    """
    :param start_x: 初始横坐标
    :param start_y: 初始纵坐标
    :param step: 行驶步数
    :param angle: 行驶角度
    :return: 新坐标
    """
    nx = start_x + step * math.cos(angle)
    ny = start_y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, float(math.pi / 6))
print(x, y)


def power(x, n):
    """
    :param x: 底数
    :param n: 基数
    :return: x^n
    """
    result = 1
    while n > 0:
        result = result * x
        n = n - 1
    return result


print('2^3: ', power(2, 3))


def calac(*numbers):
    '''
    :param numbers: list / tuple 的元素（ a，b，c……）
    :return: a2 + b2 + c2 + ……
    '''
    num_sum = 0
    for n in numbers:
        num_sum = num_sum + n * n
    return num_sum


print(calac(1, 2, 3))
nums = [1, 2, 3]
print(calac(*nums))


def person(name, age, **kw):
    '''
    :param name: 姓名
    :param age: 年龄
    :param kw: 关键字参数，可以传入0/任意个参数
    '''
    print('name: ', name, 'age: ', age, 'other: ', kw)


print(person('mike', 39))
print(person('mike2', 39, city='beijing'))
print(person('mike3', 39, city='bj', job='engineer'))


# 限制关键字参数的名字
def person2(name, age, *, city, job):
    return name, age, city, job


print(person2('jack', 24, city='beijing', job='engineer'))


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a=: ', a, 'b=: ', b, 'c= ', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)
f1(1,2,3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x='1')
f2(1,2,d=99,ext=None)


# *args 是可变参数 arg接受的是一个tuple
# **kw是关键字参数 kw接受的是dict



def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(4))

def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)













