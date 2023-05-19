#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process

EPSILON = 10 ** (-7)  # точность вычислений


def sum(x):
    n = 1
    sum = 1
    temp = x
    while abs(temp) >= EPSILON:
        sum += temp
        n += 1
        temp *= x

    print(f"Значение суммы для x={x}: {sum}")
    print(f"Проверка: 1/(1 - {x}) = {1 / (1 - x)}")


def main():
    x = 0.7

    process1 = Process(target=sum, args=(x,))
    process2 = Process(target=sum, args=(x,))

    process1.start()
    process2.start()
    process1.terminate()
    process2.terminate()


if __name__ == "__main__":
    main()
