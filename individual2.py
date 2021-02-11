#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    #Даны действительные числа x и y.
    #Найти U=max^2(x^2y,xy^2)+min^2(x-y,x+2y).
    #Для минимума и максимума использовать условный оператор if
    x = int(input("Введите X: "))
    y = int(input("Введите Y: "))
    if x * x * y < x * (y * y):
        max = x * (y * y)
    else:
        max = x * x * y
    if x - y > x + 2 * y:
        min = x + 2 * y
    else:
        min = x - y
    U = max ** 2 + min ** 2
    print(U)