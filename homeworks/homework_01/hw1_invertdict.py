#!/usr/bin/env python
# coding: utf-8


def invert(value):
    result_list = []
    if isinstance(value, list) or isinstance(value, set):
        for i in value:
            result_list += invert(i)
    else:
        result_list.append(value)
    return result_list


def invert_dict(source_dict):
    if not isinstance(source_dict, dict):
        return None
    new_dict = {}
    for key, value in source_dict.items():
        for i in invert(value):
            if i in new_dict:
                if isinstance(new_dict[i], list):
                    new_dict[i].append(key)
                else:
                    item = new_dict.get(i)
                    new_dict[i] = [item, key]
            else:
                new_dict[i] = key
    return new_dict
