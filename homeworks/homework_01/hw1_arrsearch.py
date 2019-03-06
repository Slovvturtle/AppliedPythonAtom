#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    a = {}
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
    for i in range(0, len(input_list)):
        if n - input_list[i] in a:
            return (a[n - input_list[i]], i)
        elif input_list[i] not in a:
            a[input_list[i]] = i
    return None
