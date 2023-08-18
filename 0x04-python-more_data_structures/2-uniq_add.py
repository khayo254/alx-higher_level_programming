#!/usr/bin/bash

def uniq_add(my_list = []):
    list_update = []
    for item in my_list:
        if item not in list_update:
            list_update.append(item)
    return list_update
