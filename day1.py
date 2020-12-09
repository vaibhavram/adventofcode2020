import sys

def get_int_set(filename):
    file = open(filename, "r")
    value_set = set([int(s) for s in file.readlines()])
    file.close()
    return(value_set)

def pair_product(value_set, tot):
    for value in value_set:
        if tot - value in value_set:
            return(value * (tot - value))

def trio_product(value_set, tot):
    while value_set:
        value = value_set.pop()
        pp = pair_product(value_set, tot - value)
        if pp:
            return(value * pp)

def day1(filename, tot):
    value_set = get_int_set(filename)
    pair = pair_product(value_set, tot)
    trio = trio_product(value_set, tot)
    print(pair, trio)


day1(sys.argv[1], int(sys.argv[2]))
