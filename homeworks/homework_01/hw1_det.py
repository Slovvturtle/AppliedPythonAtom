#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    a = len(list_of_lists)
    b = 0
    s = 1
    ind = 0
    for j in range(a):
        if len(list_of_lists[ind]) != a:
            return None
        ms = []
        for k in range(a - 1):
            ms.append([])
            for m in range(a):
                if m != j:
                    ms[k].append(list_of_lists[k + 1][m])

        b += s * list_of_lists[ind][j] \
            * (calculate_determinant(ms) or 1)
        s = -s

    return b
