#!/usr/bin/python3

"""
Module contains function text_indentation
And it is tested by the doctest 5-text_indentation.txt
"""


def text_indentation(text):
    """
    Formats text and by adding two lines next to every '.', '?' and ':'
    Each line printed has no space at the beginning or at the end.
    If text is not a string, TypeError is raised

    Args:
        text (str): text to be formatted
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    ft = []  # Formatted text goes here, acronym for formatted text

    #  Store each character in ft to easily delete characters
    for i in text:
        ft.append(i)

    #  If there are any spaces in the beginning of the text, clear them
    for index, item in enumerate(ft):
        if item == ' ' or item == '\t':
            ft.pop(index)
            continue
        else:
            break

    ft_len = len(ft)
    i = 0

    while i < ft_len:
        if ft[i] == '.' or ft[i] == '?' or ft[i] == ':':
            #  Clear spaces before the ., ? or : if there's any
            j = i - 1
            while j:
                if ft[j] == ' ' or ft[j] == '\t':
                    ft.pop(j)
                    j -= 1
                    ft_len -= 1
                else:
                    break
                j += 1

            #  Clear spaces after ., ? or : if there's any
            j = i + 1
            while j < ft_len:
                if ft[j] == ' ' or ft[j] == '\t':
                    ft.pop(j)
                    j -= 1
                    ft_len -= 1
                else:
                    break

            #  Add the two newlines after the ., ? or :
            ft.insert(i + 1, "\n\n")
        i += 1

    for i in ft:
        print(i, end="")
    print()
