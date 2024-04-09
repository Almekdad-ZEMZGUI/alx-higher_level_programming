#!/usr/bin/python3
"""
5-text_indentation module
with a function text_indentation
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    :param text: text to be printed with changes
    :return: nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    ind_chars = [".", "?", ":"]
    whitespace = False
    result = ""
    for char in text:
        if not whitespace and char == " ":
            continue
        whitespace = True
        result += char
        if char in ind_chars:
            result += "\n\n"
            whitespace = False
    print(result, end="")
