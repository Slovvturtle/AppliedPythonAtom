#!/usr/bin/env python
# coding: utf-8


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
    for i in range(10):
        input_string = input_string.replace(str(i) + " ", str(i) + "|")
    while " " in input_string:
        input_string = input_string.replace(" ", "")
    while "\t" in input_string:
        input_string = input_string.replace("\t", "")
    while "--" in input_string:
        input_string = input_string.replace("--", "+")
    while "++" in input_string:
        input_string = input_string.replace("++", "+")
    while "+-" in input_string:
        input_string = input_string.replace("+-", "-")
    while "(-" in input_string:
        input_string = input_string.replace("(-", "(0-")
    while "/-" in input_string:
        input_string = input_string.replace("/-", "*(0-1)/")
    while "*-" in input_string:
        input_string = input_string.replace("*-", "*(0-1)*")
    if len(input_string) > 0 and (input_string[0] is
                                  "-" or input_string[0] is "+"):
        input_string = "0" + input_string
    a = ""
    output_list = []
    b = []

    def is_op(operator):
        return (operator is "+" or operator is "-" or
                operator is "/" or operator is "*")

    while len(input_string) > 0:
        if is_op(input_string[0]):
            if len(a) > 0:
                try:
                    output_list.append(float(a))
                    a = ""
                except (TypeError, ValueError):
                    return None
            while len(b) > 0 and b[len(b) - 1] is not "(":
                if b[len(b) - 1] is '*' or input_string[0] is '+' \
                   or b[len(b) - 1] is '/' or input_string[0] is '-':
                    output_list.append(b.pop())
                else:
                    break
            b.append(input_string[0])
            input_string = input_string[1:]
        elif input_string[0] is "(":
            if len(a) > 0:
                return None
            b.append("(")
            input_string = input_string[1:]
        elif input_string[0] is ")":
            if len(a) == 0:
                return None
            try:
                output_list.append(float(a))
                a = ""
            except (TypeError, ValueError):
                return None
            input_string = input_string[1:]
            try:
                a = b.pop()
                while a is not "(":
                    output_list.append(a)
                    a = b.pop()
                a = ""
            except IndexError:
                return None
        elif input_string[0].isdigit() or input_string[0] is ".":
            a += input_string[0]
            input_string = input_string[1:]
        elif input_string[0] is "|":
            output_list.append(float(a))
            a = ""
            input_string = input_string[1:]
        else:
            return None
    if len(a) > 0:
        try:
            output_list.append(float(a))
            a = ""
        except (ValueError, TypeError):
            return None
    while len(b) > 0:
        output_list.append(b.pop())
    try:
        while len(output_list) > 0:
            a = output_list.pop(0)
            if isinstance(a, float):
                b.append(a)
            else:
                a2 = b.pop()
                a1 = b.pop()
                if a is "+":
                    b.append(a1 + a2)
                elif a is "-":
                    b.append(a1 - a2)
                elif a is "/":
                    try:
                        b.append(a1 / a2)
                    except ZeroDivisionError:
                        return None
                elif a is "*":
                    b.append(a1 * a2)
    except IndexError:
        return None
    if len(b) != 1:
        return None
    return b[0]
