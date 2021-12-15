import math


def factorialtest(test_string):
    search_list = ['[', ']', '{', '}', '@', '_', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '|', '~', '#', '<', '>', '?', '/', '\\', ':', ';', '.', '[', ']', '¬', '`']
    if search_list not in test_string:
        if test_string.isdecimal() is not None:
            return math.factorial(test_string)
