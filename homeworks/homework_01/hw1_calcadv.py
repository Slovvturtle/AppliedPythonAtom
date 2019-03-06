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
    elem = ""
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
                    elem = ""
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
                elem = ""
            except (TypeError, ValueError):
                return None
            input_string = input_string[1:]
            try:
                elem = stack.pop()
                while elem is not "(":
                    output_list.append(elem)
                    elem = stack.pop()
                elem = ""
            except IndexError:
                return None
        elif input_string[0].isdigit() or input_string[0] is ".":
            elem += input_string[0]
            input_string = input_string[1:]
        elif input_string[0] is "|":
            output_list.append(float(elem))
            elem = ""
            input_string = input_string[1:]
        else:
            return None
    if len(elem) > 0:
        try:
            output_list.append(float(elem))
            elem = ""
        except (ValueError, TypeError):
            return None
    while len(stack) > 0:
        output_list.append(stack.pop())
    try:
        while len(output_list) > 0:
            elem = output_list.pop(0)
            if isinstance(elem, float):
                stack.append(elem)
            else:
                elem2 = stack.pop()
                elem1 = stack.pop()
                if elem is "+":
                    stack.append(elem1 + elem2)
                elif elem is "-":
                    stack.append(elem1 - elem2)
                elif elem is "/":
                    try:
                        stack.append(elem1 / elem2)
                    except ZeroDivisionError:
                        return None
                elif elem is "*":
                    stack.append(elem1 * elem2)
    except IndexError:
        return None
    if len(stack) != 1:
        return None
    return stack[0]
