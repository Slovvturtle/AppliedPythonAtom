#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    if not isinstance(source_dict, dict):
        return None
    a = {}
    for key, value in source_dict.items():
        for ind in it(value):
            if ind in a:
                if isinstance(a[ind], list):
                    a[ind].append(key)
                else:
                    item = a.get(ind)
                    a[ind] = [item, key]
            else:
                a[ind] = key
    return a


def it(value):
    b = []
    if isinstance(value, list) or isinstance(value, set):
        for ind in value:
            b += it(ind)
    else:
        b.append(value)
    return b
