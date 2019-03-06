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
    stack = []

    def is_op(operator):
        return (operator is "+" or operator is "-" or
                operator is "/" or operator is "*")

    while len(input_string) > 0:
        if is_op(input_string[0]):
            if len(elem) > 0:
                try:
                    output_list.append(float(elem))
                    a = ""
                except (TypeError, ValueError):
                    return None
            while len(stack) > 0 and stack[len(stack) - 1] is not "(":
                if stack[len(stack) - 1] is '*' or input_string[0] is '+' \
                   or stack[len(stack) - 1] is '/' or input_string[0] is '-':
                    output_list.append(stack.pop())
                else:
                    break
            stack.append(input_string[0])
            input_string = input_string[1:]
        elif input_string[0] is "(":
            if len(elem) > 0:
                return None
            stack.append("(")
            input_string = input_string[1:]
        elif input_string[0] is ")":
            if len(elem) == 0:
                return None
            try:
                output_list.append(float(elem))
                a = ""
            except (TypeError, ValueError):
                return None
            input_string = input_string[1:]
            try:
                a = stack.pop()
                while a is not "(":
                    output_list.append(elem)
                    a = stack.pop()
                a = ""
            except IndexError:
                return None
        elif input_string[0].isdigit() or input_string[0] is ".":
            a += input_string[0]
            input_string = input_string[1:]
        elif input_string[0] is "|":
            output_list.append(float(elem))
            a = ""
            input_string = input_string[1:]
        else:
            return None
    if len(elem) > 0:
        try:
            output_list.append(float(elem))
            a = ""
        except (ValueError, TypeError):
            return None
    while len(stack) > 0:
        output_list.append(stack.pop())
    try:
        while len(output_list) > 0:
            a = output_list.pop(0)
            if isinstance(elem, float):
                stack.append(elem)
            else:
                elem2 = stack.pop()
                elem1 = stack.pop()
                if a is "+":
                    stack.append(elem1 + elem2)
                elif a is "-":
                    stack.append(elem1 - elem2)
                elif a is "/":
                    try:
                        stack.append(elem1 / elem2)
                    except ZeroDivisionError:
                        return None
                elif a is "*":
                    stack.append(elem1 * elem2)
    except IndexError:
        return None
    if len(stack) != 1:
        return None
    return stack[0]
