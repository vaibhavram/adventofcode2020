import sys

def get_mountain(filename):
    file = open(filename, "r")
    mountain = [row[0:(len(row)-1)] for row in file.readlines()]
    file.close()
    return mountain

def count_trees(mountain, across, down):
    tree_counter = 0
    x = 0
    y = 0
    mountain_width = len(mountain[0])
    mountain_length = len(mountain)
    while y < mountain_length - 1:
        x += across
        y += down
        if mountain[y][x % mountain_width] == '#':
            tree_counter += 1
    return tree_counter

def array_prod(arr):
    prod = 1
    for elem in arr:
        prod *= elem
    return prod

def slope_products(mountain, acrosses, downs):
    num_trees = [count_trees(mountain, acrosses[i], downs[i]) for i in range(len(acrosses))]
    return array_prod(num_trees)

def main(filename):
    mountain = get_mountain(filename)
    num_trees = count_trees(mountain, 3, 1)
    slope_prod = slope_products(mountain, [1, 3, 5, 7, 1], [1, 1, 1, 1, 2])
    print(num_trees, slope_prod)

main(sys.argv[1])