# -*- coding: utf-8 -*-
#九九乘法表

i = 1
while i:
    j = 1
    while j:
        print( j, "*", i, " = ", i * j, '  ',)
        if i == j:
            break

        j += 1
        if j >= 10:
            break
    i += 1
    if i >= 10:
        break