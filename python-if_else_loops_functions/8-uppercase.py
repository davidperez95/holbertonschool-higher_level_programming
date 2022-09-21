#!/usr/bin/python3
def uppercase(str):
    upper_string = ''
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            upper_string += chr(ord(str[i]) - 32)
            continue
        upper_string += str[i]

    print("{}".format(upper_string))
