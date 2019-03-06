#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    a = []
    for i in input_string:
        if i not in set('({[)}]'):
            continue
        if i in set('({['):
            a.append(i)
            continue
        if len(a) == 0:
            return False
        openingBracket = a.pop()
        if (not (
                (openingBracket == '{' and i == '}') or
                (openingBracket == '[' and i == ']') or
                (openingBracket == '(' and i == ')')
                )):
            return False
    if 0 != len(a):
        return False
    return True
