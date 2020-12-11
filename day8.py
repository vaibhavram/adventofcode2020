import sys
import re

def get_code(filename):
    file = open(filename, "r")
    code = [re.sub("\n", "", line) for line in file.readlines()]
    return(code)

def parse_code(line):
    split = line.split()
    command = split[0]
    number = int(split[1][1:]) * (-1 if split[1][0] == "-" else 1)
    return(command, number)

def get_acc_prior_inf(code):
    lines_run = set()
    accumulator = 0
    curr_line = 0
    while curr_line not in lines_run:
        lines_run.add(curr_line)
        parse = parse_code(code[curr_line])
        if parse[0] == "acc":
            accumulator += parse[1]
            curr_line += 1
        elif parse[0] == "jmp":
            curr_line += parse[1]
        else:
            curr_line += 1
    return(accumulator)

def terminates(code):
    lines_run = set()
    accumulator = 0
    curr_line = 0
    while curr_line not in lines_run and curr_line < len(code):
        lines_run.add(curr_line)
        parse = parse_code(code[curr_line])
        if parse[0] == "acc":
            accumulator += parse[1]
            curr_line += 1
        elif parse[0] == "jmp":
            curr_line += parse[1]
        else:
            curr_line += 1
    if curr_line == len(code):
        return(accumulator)

def try_changes(code):
    for i in range(len(code)):
        temp = [elem for elem in code]
        changed = False
        if code[i].startswith("nop"):
            temp[i] = "jmp" + code[i][3:]
            changed = True
        elif code[i].startswith("jmp"):
            temp[i] = "nop" + code[i][3:]
            changed = True
        if changed:
            terminated = terminates(temp)
            if terminated:
                return(terminated)

def main(filename):
    code = get_code(filename)
    acc_prior_inf = get_acc_prior_inf(code)
    acc_after_termination = try_changes(code)
    print(acc_prior_inf, acc_after_termination)

main(sys.argv[1])