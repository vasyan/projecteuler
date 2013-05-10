# -*- encoding: utf-8 -*-
"""
Решение четвертой задачи из Проекта Эйлер
http://projecteuler.net/problem=4
---
Создание генератора кандидатов в полиндромы, проверка, нахождение максимума
"""

from itertools import ifilter


def candidates():
    for i in xrange(900, 999):
        for j in xrange(900, 999):
            yield i * j


def is_palindrome(number):
    s = str(number)
    return s[:len(s)/2] == s[-1:len(s)/2 - 1:-1]


def main():
    print "Max palindrome = %d" % max(
        ifilter(
            is_palindrome,
            candidates()
        )
    )


if __name__ == '__main__':
    main()
