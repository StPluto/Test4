#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    #Найти все трехзначные натуральные числа, сумма цифр которых равна их произведению.
    for i in range(1, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                if i + j + k == i * j * k:
                    print(f"{i}{j}{k}")