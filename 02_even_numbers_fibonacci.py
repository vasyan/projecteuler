# -*- encoding: utf-8 -*-
"""
Решение второй задачи из Проекта Эйлер
http://projecteuler.net/problem=2
---
Создание генератора последовательности фибоначи и суммирование ее членов по условию четности
"""


LIMIT = 4000000


def fibonacci(a=1, b=2):
    while b < LIMIT:
        yield b
        a, b = b, a + b


def main():
    print "Summ = %s" % sum(
        filter(
            lambda i: i % 2 == 0,
            fibonacci()
        )
    )


if __name__ == '__main__':
    main()