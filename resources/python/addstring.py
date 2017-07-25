__author__ = 'inatiwari'

def join_two_string(arg1,arg2):
    return arg1 + " " + arg2

def validnumber(number):
    if not number[:2].isalpha():
        raise ValueError("No Airline code in '{}'".format(number))

    if not number[:2].isupper():
        raise ValueError("Invalid Airline code is '{}'".format(number))

    if not (number[2:].isdigit() and int(number[2:]) <= 9999):
        raise ValueError("Invalid Route Number '{}".format(number))

    return number