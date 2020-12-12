import sys
import re

def get_layout(filename):
    file = open(filename, "r")
    layout = [[char for char in re.sub("\n", "", line)] for line in file.readlines()]
    return(layout)

def num_adj_occ(layout, i, j):
    n = len(layout)
    m = len(layout[0])
    adj = []
    for k in range(max(0, i-1), min(n, i+2)):
        for l in range(max(0, j-1), min(m, j+2)):
            if not (k == i and l == j):
                adj.append(layout[k][l])
    return sum([elem == "#" for elem in adj])

def mutate_layout(layout):
    copy = [[seat for seat in row] for row in layout]
    mutations = {"L": [], "#": []}
    for i in range(len(layout)):
        for j in range(len(layout[0])):
            if layout[i][j] == "#" and num_adj_occ(layout, i, j) >= 4:
                mutations["#"].append((i,j))
            elif layout[i][j] == "L" and num_adj_occ(layout, i, j) == 0:
                mutations["L"].append((i,j))
    for tup in mutations["L"]:
        copy[tup[0]][tup[1]] = "#"
    for tup in mutations["#"]:
        copy[tup[0]][tup[1]] = "L"
    return copy

def count_occ(layout):
    ct = 0
    for row in layout:
        for seat in row:
            ct += 1 if seat == "#" else 0
    return(ct)

def iterate(layout):
    prev = [["." for seat in row] for row in layout]
    new = [[seat for seat in row] for row in layout]
    while new != prev:
        prev = new # .copy()?
        new = mutate_layout(prev)
    return count_occ(new)

def main(filename):
    layout = get_layout(filename)
    terminal_count = iterate(layout)
    print(terminal_count)

main(sys.argv[1])