import sys
import re
import math

def get_data(filename):
    file = open(filename, "r")
    data = []
    for line in file.readlines():
        if line.startswith("mask"):
            data.append(tuple(re.sub("\n", "", line).split(" = ")))
        elif line.startswith("mem"):
            split1 = re.sub("\\]", "", re.sub("\n", "", line)).split(" = ")
            split2 = split1[0].split("[")
            data.append(tuple([split2[0], int(split2[1]), int(split1[1])]))
    return data

def apply_mask1(mask, num):
    val = 0
    for i in range(len(mask)):
        if (mask[i] == "X" and (num >> i) % 2 == 1) or (mask[i] != "X" and mask[i] == 1):
            val += math.pow(2, i)
    return int(val)

def apply_mask2(mask, num):
    vals = [0]
    for i in range(len(mask)):
        if mask[i] == "X":
            vals = vals + [val + math.pow(2, i) for val in vals]
        elif mask[i] == 1 or (num >> i) % 2 == 1:
            vals = [val + math.pow(2, i) for val in vals]
    return [int(i) for i in vals]

def process_data1(data):
    mask = [0]*36
    memory = {}
    for line in data:
        if line[0] == "mask":
            mask = [int(bit) if bit != "X" else "X" for bit in list(reversed(line[1]))]
        elif line[0] == "mem":
            memory[line[1]] = apply_mask1(mask, line[2])
    return sum(memory.values())

def process_data2(data):
    mask = [0]*36
    memory = {}
    for line in data:
        if line[0] == "mask":
            mask = [int(bit) if bit != "X" else "X" for bit in list(reversed(line[1]))]
        elif line[0] == "mem":
            addresses = apply_mask2(mask, line[1])
            for address in addresses:
                memory[address] = line[2]
    return sum(memory.values())

def main(filename):
    data = get_data(filename)
    total1 = process_data1(data)
    total2 = process_data2(data)
    print(total1, total2)

main(sys.argv[1])