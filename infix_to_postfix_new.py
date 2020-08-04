#!/bin/python3
import tabulate


def infix_postfix_non_boolean(input_infix):
    table_list = []
    if not isinstance(input_infix, str):
        raise TypeError("This function takes only string as argument")
    input_char_list = [char for char in input_infix if not char.isspace()]
    output = ""
    stack = ["("]
    table_list.append(["start", str(stack), output])
    for char in input_char_list:
        if char.isalnum():
            output += char
        elif char in "()*^/+-":
            if char == ")":
                while True:
                    stack_char = stack.pop()
                    if stack_char == "(":
                        break
                    output += stack_char
            elif char == "(":
                stack.append(char)
            elif char in "+-":
                while True:
                    stack_char = stack.pop()
                    if stack_char == "(":
                        stack.append(stack_char)
                        break
                    output += stack_char
                stack.append(char)
            elif char in "*/":
                while True:
                    stack_char = stack.pop()
                    if stack_char in "(+-":
                        stack.append(stack_char)
                        break
                    output += stack_char
                stack.append(char)
            elif char in "^":
                stack.append(char)
            else:
                raise RuntimeError("Unknown Operator")
        else:
            raise ("Unknown character")
        table_list.append(["'" + char + "'", str(stack), output])
    char = ""
    while len(stack) > 1:
        stack_char = stack.pop()
        output += stack_char
        table_list.append(["end", str(stack), output])
    table = tabulate.tabulate(table_list)
    print(table)


def infix_postfix_boolean(input_infix):
    table_list = []
    if not isinstance(input_infix, str):
        raise TypeError("This function takes only string as argument")
    input_word_list = input_infix.split()
    output = ""
    stack = ["("]
    table_list.append(["start", str(stack), output])
    for word in input_word_list:
        if word not in ("NOT", "AND", "OR", "(", ")"):
            output += word + " "
        elif word in ("NOT", "AND", "OR", "(", ")"):
            if word == ")":
                while True:
                    stack_word = stack.pop()
                    if stack_word == "(":
                        break
                    output += stack_word + " "
            elif word == "(":
                stack.append(word)
            elif word in ("AND", "OR"):
                while True:
                    stack_word = stack.pop()
                    if stack_word in "(":
                        stack.append(stack_word)
                        break
                    output += stack_word + " "
                stack.append(word)
            elif word == "NOT":
                stack.append(word)
            else:
                raise RuntimeError("Unknown Operator")
        else:
            raise ("Unknown operator")
        table_list.append(["'" + word + "'", str(stack), output])
    word = ""
    while len(stack) > 1:
        stack_word = stack.pop()
        output += stack_word + " "
        table_list.append(["end", str(stack), output])
    table = tabulate.tabulate(table_list)
    print(table)


if __name__ == "__main__":
    try:
        while True:
            input_str = input("> ")
            for check in ("AND", "OR", "NOT"):
                if check in input_str.upper():
                    infix_postfix_boolean(input_str)
                    break
            else:
                infix_postfix_non_boolean(input_str)
    except (EOFError, KeyboardInterrupt):
        print()
        exit(0)
