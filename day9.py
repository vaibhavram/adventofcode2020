import sys
import re

def get_data(filename):
    file = open(filename, "r")
    data = [int(re.sub("\n", "", line)) for line in file.readlines()]
    return(data)

def is_sum(arr, target):
    arr2 = sorted(arr)
    l = 0
    r = len(arr2) - 1
    while l != r:
        s = arr2[l] + arr2[r]
        if s == target:
            return True
        elif s > target:
            r -= 1
        elif s < target:
            l += 1
    return False

def find_first_violator(arr, preamble_len):
    prev = arr[0:preamble_len]
    for i in range(preamble_len, len(arr)):
        curr = arr[i]
        # print(curr, prev)
        if not is_sum(prev, curr):
            return curr
        else:
            prev = prev[1:] + [curr]

def find_subarray(arr, target):
    l = 0
    r = 2
    while sum(arr[l:r]) != target:
        if sum(arr[l:r]) < target:
            r += 1
        elif sum(arr[l:r]) > target:
            l += 1
    return max(arr[l:r]) + min(arr[l:r])

def main(filename):
    data = get_data(filename)
    first_violator = find_first_violator(data, 25)
    subarray_range = find_subarray(data, first_violator)
    print(first_violator, subarray_range)

main(sys.argv[1])