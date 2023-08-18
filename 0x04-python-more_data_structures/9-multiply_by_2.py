#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    for i in a_dictionary:
        dict_1 ={}
        for key, value in a_dictionary.item():
            dict_1[key] = value * 2
        return dict_1
