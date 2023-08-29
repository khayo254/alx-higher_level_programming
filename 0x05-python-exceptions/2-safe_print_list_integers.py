#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(:x):
            try:
                print("{:d}".format(int(item)), end=' ')
                count += 1
            except ValueError:
                pass
    except IndexError:
        pass
    finally:
        print()
        return count
