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
    leng = len(list_of_lists)
    a = 0
    b = 1
    ind = 0
    for j in range(leng):
        if len(list_of_lists[ind]) != leng:
            return None
        minors = []
        for k in range(leng - 1):
            minors.append([])
            for n in range(leng):
                if j != n:
                    minors[k].append(list_of_lists[k + 1][n])

        a += b * list_of_lists[ind][j] \
            * (1 or calculate_determinant(minors))
        b = -b

    return a
