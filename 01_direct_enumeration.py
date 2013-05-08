# -*- encoding: utf-8 -*-
"""
Решение первой задачи из Проекта Эйлер
http://projecteuler.net/problem=1
---
Праямой перебор натурального ряда, проверка на делимость и суммирование 
"""

LIMIT = 1000


def main():    
    counter = 1
    summ = 0
    while counter < LIMIT:
        if counter % 3 == 0:
            summ += counter
        elif counter % 5 == 0:
            summ += counter

        counter += 1

    print "Summ = %d" % summ


if __name__ == '__main__':
    main()