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

def num_sightline_occ(layout, i, j):
    n = len(layout)
    m = len(layout[0])
    sightlines = []
    for x in [0,1,-1]:
        for y in [0,1,-1]:
            if not (x == 0 and y == 0):
                k = i + x
                l = j + y
                while 0 <= k <= n - 1 and 0 <= l <= m - 1:
                    if layout[k][l] != ".":
                        sightlines.append(layout[k][l])
                        k = -1
                        l = -1
                    else:
                        k += x
                        l += y
    return sum([elem == "#" for elem in sightlines])

def mutate_layout(layout, adj_func, thresh):
    copy = [[seat for seat in row] for row in layout]
    mutations = {"L": [], "#": []}
    for i in range(len(layout)):
        for j in range(len(layout[0])):
            if layout[i][j] == "#" and adj_func(layout, i, j) >= thresh:
                mutations["#"].append((i,j))
            elif layout[i][j] == "L" and adj_func(layout, i, j) == 0:
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

def iterate(layout, adj_func, thresh):
    prev = [["." for seat in row] for row in layout]
    new = [[seat for seat in row] for row in layout]
    while new != prev:
        prev = new
        new = mutate_layout(prev, adj_func, thresh)
    return count_occ(new)

def main(filename):
    layout = get_layout(filename)
    terminal_count1 = iterate(layout, num_adj_occ, 4)
    terminal_count2 = iterate(layout, num_sightline_occ, 5)
    print(terminal_count1, terminal_count2)

main(sys.argv[1])