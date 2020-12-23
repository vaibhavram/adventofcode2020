import sys
import re
import operator

def parse_formula(formula):
    formula = re.sub(" ", "", formula)
    return [char for char in formula]

def get_formulas(filename):
    file = open(filename, "r")
    formulas = [parse_formula(re.sub("\n", "", line)) for line in file.readlines()]
    file.close()
    return formulas

def evaluate_formula(formula):
    functions = {'+': operator.add, '*': operator.mul}
    started = False
    i = 0
    while i < len(formula):
        # print("index i =", i)
        if not started:
            lag = 1
            inc = 0
            if formula[i] == '(':
                result, inc = evaluate_formula(formula[(i + 1):])
            else :
                result = int(formula[i])
            started = True
            i += lag + inc
        else:
            try:
                lag = 0
                next_op = formula[i]
                # print("next op:", next_op)
                if next_op == ')':
                    # print("exiting parenthetical at i =", i)
                    return (result, i + 1)
                next_num = formula[i + 1]
                if next_num == '(':
                    # print("entering parenthetical at i =", i + 1)
                    next_num, lag = evaluate_formula(formula[(i + 2):])
                result = functions[next_op](result, int(next_num))
                # print("incrementing i by", 2 + lag)
                i += 2 + lag
            except IndexError:
                return (result, 0)
    return (result, 0)

def sum_formulas(formulas):
    s = 0
    for formula in formulas:
        # print(formula)
        s += evaluate_formula(formula)[0]
    return s

def main(filename):
    formulas = get_formulas(filename)
    formulas_sum = sum_formulas(formulas)
    print(formulas_sum)

main(sys.argv[1])