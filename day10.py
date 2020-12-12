import sys
import re

def get_adaptors(filename):
    file = open(filename, "r")
    adaptors = [int(re.sub("\n", "", line)) for line in file.readlines()]
    return(adaptors)

def sort_adaptors(adaptors):
    return [0] + sorted(adaptors) + [max(adaptors) + 3]

def get_prod_1j_3j(adaptors):
    diffs = {}
    for i in range(1, len(adaptors)):
        diff = adaptors[i] - adaptors[i - 1]
        diffs[diff] = diffs.get(diff, 0) + 1
    return diffs[1] * diffs[3]

def get_arrangements(adaptors, memo):
    if len(adaptors) == 2:
        return 1
    else:
        num_next = sum([a - adaptors[0] <= 3 for a in adaptors[1:]])
        arrangements = 0
        for i in range(num_next):
            if adaptors[i+1] in memo.keys():
                arrangements += memo[adaptors[i+1]]
            else:
                s = get_arrangements(adaptors[(i+1):], memo)
                memo[adaptors[i+1]] = s 
                arrangements += s
        return arrangements

def main(filename):
    adaptors = sort_adaptors(get_adaptors(filename))
    prod_1j_3j = get_prod_1j_3j(adaptors)
    arrangements = get_arrangements(adaptors, {})
    print(prod_1j_3j, arrangements)

main(sys.argv[1])