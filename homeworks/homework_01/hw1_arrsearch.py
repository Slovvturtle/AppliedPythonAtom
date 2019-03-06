#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    
    '''
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''
    lookup = {}
    for index in range(0, len(input_list)):
            if n - input_list[index] in lookup:
            return (lookup[n - input_list[index]], index)
        elif input_list[index] not in lookup:
            lookup[input_list[index]] = index
    return None
